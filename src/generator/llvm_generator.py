from antlr4 import *
from llvmlite import ir
from generator.parse_exception import *
from generator.symbol_table import SymbolTable
from generator.type import *
from maverick_parser.MaverickLexer import MaverickLexer
from maverick_parser.MaverickParser import MaverickParser
from maverick_parser.MaverickVisitor import MaverickVisitor



class MVisitor(MaverickVisitor):

    def __init__(self, triple, data_layout):
        super(MaverickVisitor, self).__init__()
        self.module = ir.Module()
        self.module.triple = triple
        self.module.data_layout = data_layout

        # function block list
        self.block_list = []
        #
        self.builder_list = []
        # used to store function, key: function name, value: ir.Function
        self.func_list = dict()

        self.cur_endif_block = None

        self.symbol_table = SymbolTable()

        self.need_load = True

        self.constants = 0

        func_name = 'main';
        llvm_type = ir.FunctionType(nil, [])
        llvm_func = ir.Function(self.module, llvm_type, name=func_name)
        block = llvm_func.append_basic_block(name=func_name + '.entry')
        self.block_list.append(block)
        self.func_list[func_name] = llvm_func
        builder = ir.IRBuilder(block)
        self.builder_list.append(builder)

        # init printf/scanf function
        printf_type = ir.FunctionType(int32, [ir.PointerType(byte)], var_arg=True)
        printf = ir.Function(self.module, printf_type, name="printf")
        self.func_list['printf'] = printf

        scanf_type = ir.FunctionType(int32, [ir.PointerType(byte)], var_arg=True)
        scanf = ir.Function(self.module, scanf_type, name="scanf")
        self.func_list['scanf'] = scanf

    def save(self, filename):
        """
        Param filename: LLVM compiled filename
        """
        with open(filename, "w") as f:
            f.write(repr(self.module))

    def newBlock(self, block):
        self.block_list.pop()
        self.block_list.append(block)
        self.builder_list.pop()
        self.builder_list.append(ir.IRBuilder(block))

    def visitStat(self, ctx: MaverickParser.StatContext):
        if ctx.getChild(0).getText() == ';':
            print(';')
        if ctx.getChild(0).getText() == 'function':
            funcname = ctx.getChild(1).getText()
            print(funcname)
            self.visit(ctx.getChild(2))
        return super().visitStat(ctx)

    def visitVarinit(self, ctx: MaverickParser.VarinitContext):
        varlist_ctx = ctx.getChild(0)
        var_length = int((varlist_ctx.getChildCount() - 1) / 2 + 1)
        explist_ctx = ctx.getChild(2)
        exp_length = int((explist_ctx.getChildCount() - 1) / 2 + 1)
        explist = self.visit(explist_ctx)
        for i in range(0, var_length, 1):
            id = varlist_ctx.getChild(2 * i).getText()
            if (i < exp_length):
                val = explist[i]
                if self.symbol_table.is_global():
                    mvar = ir.GlobalVariable(self.module, val['type'], name=id)
                    mvar.linkage = 'internal'
                    mvar.initializer = ir.Constant(val['type'], val['name'].constant)
                else:
                    mvar = self.builder_list[-1].alloca(val['type'], name=id)
                    self.builder_list[-1].store(val['name'], mvar)
                self.symbol_table.insert_item(id, {'Type': val['type'], 'Name': mvar})
            else:
                raise InitializationException(id)
        need_load_cache = self.need_load
        self.need_load = False
        super().visitVarinit(ctx)
        self.need_load = need_load_cache

    def visitFunctiondef(self, ctx: MaverickParser.FunctiondefContext):
        return super().visitFunctiondef(ctx)

    def visitLocalfuncdef(self, ctx: MaverickParser.LocalfuncdefContext):
        return super().visitLocalfuncdef(ctx)

    def visitExplist(self, ctx: MaverickParser.ExplistContext):
        exp_length = int((ctx.getChildCount() - 1) / 2 + 1)
        explist = []
        for i in range(0, exp_length, 1):
            explist.append(self.visit(ctx.getChild(2 * i)))
        return explist

    def visitExp(self, ctx: MaverickParser.ExpContext):
        if ctx.getChild(0).getText() == 'nil':
            return {
                'type': nil,
                'const': False,
                'name': ir.Constant(nil, None)
            }
        elif ctx.getChild(0).getText() == 'false':
            return {
                'type': boolean,
                'const': False,
                'name': ir.Constant(boolean, 0)
            }
        elif ctx.getChild(0).getText() == 'true':
            return {
                'type': boolean,
                'const': False,
                'name': ir.Constant(boolean, 1)
            }
        return super().visitExp(ctx)

    def visitVar(self, ctx: MaverickParser.VarContext):
        id = ctx.getText()
        if not self.symbol_table.has_item(id):
            return {
                'type': int32,
                'const': False,
                'name': ir.Constant(int32, None)
            }
        builder = self.builder_list[-1]
        item = self.symbol_table.get_item(id)
        if item is not None:
            if self.need_load:
                return {
                    "type": item["Type"],
                    "const": False,
                    "name": builder.load(item["Name"]),
                }
            else:
                return {
                    "type": item["Type"],
                    "const": False,
                    "name": item["Name"],
                }
        else:
            return {
                'type': nil,
                'const': False,
                'name': ir.Constant(nil, None)
            }

    def visitLaststat(self, ctx: MaverickParser.LaststatContext):
        return super().visitLaststat(ctx)

    def visitMyINT(self, ctx: MaverickParser.MyINTContext):
        return {
            'type': int32,
            'const': True,
            'name': ir.Constant(int32, int(ctx.getText()))
        }

    def visitMyHEX(self, ctx: MaverickParser.MyHEXContext):
        return {
            'type': int32,
            'const': True,
            'name': ir.Constant(int32, int(ctx.getText(), 16))
        }

    def visitMyFLOAT(self, ctx: MaverickParser.MyFLOATContext):
        return {
            'type': float,
            'const': True,
            'name': ir.Constant(float, int(ctx.getText()))
        }

    def visitString(self, ctx: MaverickParser.StringContext):
        """
        mySTRING: STRING;
        """
        mstr = ctx.getText().replace('\\n', '\n')[1:-1] + '\0'
        length = len(bytearray(mstr, 'utf-8'))
        ret = ir.GlobalVariable(self.module, ir.ArrayType(byte, length), ".str%d" % self.
                                constants)
        self.constants += 1
        ret.global_constant = True
        ret.initializer = ir.Constant(ir.ArrayType(byte, length), bytearray(mstr, 'utf-8'))
        return {
            'type': ir.ArrayType(byte, length),
            'const': False,
            'name': ret
        }

    def visitPrintfFunction(self, ctx: MaverickParser.PrintfFunctionContext):
        printf = self.func_list['printf']
        builder = self.builder_list[-1]
        zero = ir.Constant(int32, 0)
        arg_list = [builder.gep(self.visit(ctx.getChild(2))['name'], [zero, zero], inbounds=True)]
        length = ctx.getChildCount()
        for i in range(4, length - 1, 2):
            arg_list.append(self.visit(ctx.getChild(i))['name'])
        return {
            'type': int32,
            'name': builder.call(printf, arg_list)
        }

    def visitScanfFunction(self, ctx: MaverickParser.ScanfFunctionContext):
        scanf = self.func_list['scanf']
        builder = self.builder_list[-1]
        zero = ir.Constant(int32, 0)
        arg_list = [builder.gep(self.visit(ctx.getChild(2))['name'], [zero, zero], inbounds=True)]
        length = ctx.getChildCount()
        for i in range(4, length - 1, 2):
            need_load_cache = self.need_load
            self.need_load = False
            arg_list.append(self.visit(ctx.getChild(i))['name'])
            self.need_load = need_load_cache
        return {
            'type': int32,
            'name': builder.call(scanf, arg_list)
        }

def generate(input_filename, output_filename, triple, data_layout):
    """
    Param input_filename: Maverick Source filename
    Param output_filename: LLVM compiled filename
    Param triple:
    Param data_layout:
    """
    lexer = MaverickLexer(FileStream(input_filename))
    stream = CommonTokenStream(lexer)
    parser = MaverickParser(stream)
    parser.removeErrorListeners()
    # errorListener = syntaxErrorListener()
    # parser.addErrorListener(errorListener)

    tree = parser.chunk()
    v = MVisitor(triple, data_layout)
    v.visit(tree)
    v.builder_list[0].ret_void()
    v.save(output_filename)
