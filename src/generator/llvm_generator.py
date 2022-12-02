from antlr4 import *
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
        # used to store control condition block
        self.ctr_cond_list = []
        # used to store control end block
        self.ctr_end_list = []
        self.cur_endif_block = None

        self.symbol_table = SymbolTable()

        self.need_load = True

        self.constants = 0

        func_name = 'main';
        llvm_type = ir.FunctionType(void, [])
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
        
    def value2Boolean(self, var, not_equal=True):
        builder = self.builder_list[-1]
        operator = "==" if not_equal else "!="
        return_dict = {
            'type': boolean,
            'const': False
        }
        if var['type'] == byte or var['type'] == int32:
            return_dict["name"] = builder.icmp_signed(operator, var['name'],
                                                      ir.Constant(var['type'], 0))
            return return_dict
        elif var['type'] == float:
            return_dict["name"] = builder.fcmp_ordered(operator, var['name'], ir.Constant(float, 0))
            return return_dict
        return var

    def exprConvert(self, expr1, expr_right):
        if expr1['type'] == expr_right['type']:
            return expr1, expr_right
        else:
            raise TypeMisatchException(expr1, expr_right)
        return expr1, expr_right

    def get_return_dict(self, ctx):
        expr_left = self.visit(ctx.getChild(0))
        expr_right = self.visit(ctx.getChild(2))
        expr1, expr2 = self.exprConvert(expr_left, expr_right)
        return_dict = {
            'type': expr1['type'],
            'const': False
        }
        return expr1, expr2, return_dict

    def visitBlock(self, ctx: MaverickParser.BlockContext):
        return super().visitBlock(ctx)

    def visitStat(self, ctx: MaverickParser.StatContext):
        if ctx.getChild(0).getText() == ';':
            print(';')
        if ctx.getChild(0).getText() == 'function':
            funcname = ctx.getChild(1).getText()
            print(funcname)
            self.visit(ctx.getChild(2))
        return super().visitStat(ctx)

    def visitType(self, ctx: MaverickParser.TypeContext):
        if ctx.getText() == 'byte':
            return byte
        if ctx.getText() == 'boolean':
            return boolean
        if ctx.getText() == 'int':
            return int32
        if ctx.getText() == 'float':
            return float
        return void

    def visitVarinit(self, ctx: MaverickParser.VarinitContext):
        varlist_ctx = ctx.getChild(1)
        explist_ctx = ctx.getChild(3)
        var_length = int((varlist_ctx.getChildCount() - 1) / 2 + 1)
        exp_length = int((explist_ctx.getChildCount() - 1) / 2 + 1)
        explist = self.visit(explist_ctx)
        for i in range(0, var_length, 1):
            id = varlist_ctx.getChild(2 * i).getText()
            if (i < exp_length):
                val = explist[i]
                if self.symbol_table.is_global():
                    var = ir.GlobalVariable(self.module, val['type'], name=id)
                    var.linkage = 'internal'
                    var.initializer = ir.Constant(val['type'], val['name'].constant)
                else:
                    var = self.builder_list[-1].alloca(val['type'], name=id)
                    self.builder_list[-1].store(val['name'], var)
                self.symbol_table.insert_item(id, {'Type': val['type'], 'Name': var})
            else:
                raise InitializationException(id)

    def visitVarassign(self, ctx: MaverickParser.VarassignContext):
        builder = self.builder_list[-1]
        val = self.visit(ctx.getChild(2))
        need_load_cache = self.need_load
        self.need_load = False
        var = self.visit(ctx.getChild(0))
        self.need_load = need_load_cache
        builder.store(val['name'], var['name'])
        return {'type': var['type'], 'name': builder.load(var['name'])}

    def visitFuncdef(self, ctx: MaverickParser.FuncdefContext):
        """
        funcdef: 'function' type funcname '(' parlist? ')' funcbody
        """
        # funcname
        func_name = ctx.getChild(2).getText()
        if func_name in self.func_list:
            raise FunctionNameDuplicateException(func_name=func_name)
        return_type = self.visit(ctx.getChild(1))
        # func params
        para_list = self.visit(ctx.getChild(4))
        type_list = []
        for i in range(len(para_list)):
            type_list.append(para_list[i]['type'])
        llvm_type = ir.FunctionType(return_type, type_list)
        llvm_func = ir.Function(self.module, llvm_type, name=func_name)
        for i in range(len(para_list)):
            llvm_func.args[i].name = para_list[i]['name']
        block = llvm_func.append_basic_block(name=func_name + '.entry')
        self.block_list.append(block)
        self.func_list[func_name] = llvm_func
        builder = ir.IRBuilder(block)
        self.builder_list.append(builder)
        self.cur_func = func_name
        self.symbol_table.func_enter()
        for i in range(len(para_list)):
            mvar = builder.alloca(para_list[i]['type'])
            builder.store(llvm_func.args[i], mvar)
            self.symbol_table.insert_item(para_list[i]['name'], {'Type': para_list[i]['type'], 'Name': mvar})
        self.visit(ctx.getChild(ctx.getChildCount() - 1))  # funcbody
        self.cur_func = ''
        self.block_list.pop()
        self.builder_list.pop()
        self.symbol_table.func_quit()

    def visitParlist(self, ctx: MaverickParser.ParlistContext):
        """
        return param list
        """
        return self.visit(ctx.getChild(0))

    def visitNamelist(self, ctx: MaverickParser.NamelistContext):
        """
        return name list
        """
        length = ctx.getChildCount()
        param_list = []
        for i in range(0, length, 3):
            param = {
                'type': self.visit(ctx.getChild(i)),
                'name': ctx.getChild(i+1).getText()
            }
            param_list.append(param)
        return param_list

    def visitWhileblock(self, ctx: MaverickParser.WhileblockContext):
        """
        whileblock
            : 'while' condition 'do' block 'end'
            ;
        """
        self.symbol_table.func_enter()
        cur_builder = self.builder_list[-1]
        cond_block = cur_builder.append_basic_block()
        body_block = cur_builder.append_basic_block()
        endwhile_block = cur_builder.append_basic_block()
        self.ctr_cond_list.append(cond_block)
        self.ctr_end_list.append(endwhile_block)

        cur_builder.branch(cond_block)
        self.newBlock(cond_block)
        cond = self.visit(ctx.getChild(1))

        self.builder_list[-1].cbranch(cond['name'], body_block, endwhile_block)
        self.newBlock(body_block)
        self.visit(ctx.getChild(3))

        try:
            self.builder_list[-1].branch(cond_block)
        except AssertionError:
            print("Branch optimize")

        self.newBlock(endwhile_block)
        self.ctr_cond_list.pop(-1)
        self.ctr_end_list.pop(-1)
        self.symbol_table.func_quit()

    def visitRepeatblock(self, ctx: MaverickParser.RepeatblockContext):
        """
        repeatblock
            : 'repeat' block 'until' condition
            ;
        """
        self.symbol_table.func_enter()
        cur_builder = self.builder_list[-1]
        cond_block = cur_builder.append_basic_block()
        body_block = cur_builder.append_basic_block()
        endwhile_block = cur_builder.append_basic_block()
        self.ctr_cond_list.append(cond_block)
        self.ctr_end_list.append(endwhile_block)

        cur_builder.branch(cond_block)
        self.newBlock(cond_block)
        cond = self.visit(ctx.getChild(3))

        self.builder_list[-1].cbranch(cond['name'], body_block, endwhile_block)
        self.newBlock(body_block)
        self.visit(ctx.getChild(2))

        try:
            self.builder_list[-1].branch(cond_block)
        except AssertionError:
            print("Branch optimize")

        self.newBlock(endwhile_block)
        self.ctr_cond_list.pop(-1)
        self.ctr_end_list.pop(-1)
        self.symbol_table.func_quit()


    def visitForblock(self, ctx: MaverickParser.ForequalblockContext):
        return super().visitForequalblock(ctx)

    def visitIfblock(self, ctx: MaverickParser.IfblockContext):
        """
        ifblock
        : 'if' condition 'then' block ('elseif' condition 'then' block)* ('else' block)? 'end'
        ;
        """
        cur_builder = self.builder_list[-1]
        if_block = cur_builder.append_basic_block()
        endif_block = cur_builder.append_basic_block()

        cache = self.cur_endif_block
        self.cur_endif_block = endif_block

        cur_builder.branch(if_block)
        self.newBlock(if_block)

        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))

        if not self.block_list[-1].is_terminated:
            self.builder_list[-1].branch(endif_block)
        self.cur_endif_block = cache
        self.newBlock(endif_block)

    def visitIfconditionblock(self, ctx: MaverickParser.IfconditionblockContext):
        self.symbol_table.func_enter()
        cur_builder = self.builder_list[-1]
        true_block = cur_builder.append_basic_block()
        false_block = cur_builder.append_basic_block()

        cur_builder.cbranch(self.visit(ctx.getChild(1))['name'], true_block, false_block)
        self.newBlock(true_block)
        self.visit(ctx.getChild(3))

        if not self.block_list[-1].is_terminated:
            self.builder_list[-1].branch(self.cur_endif_block)
        self.newBlock(false_block)
        self.symbol_table.func_quit()

    def visitElseifconditionblock(self, ctx: MaverickParser.ElseifconditionblockContext):
        self.symbol_table.func_enter()
        cur_builder = self.builder_list[-1]
        true_block = cur_builder.append_basic_block()
        false_block = cur_builder.append_basic_block()

        cur_builder.cbranch(self.visit(ctx.getChild(1))['name'], true_block, false_block)
        self.newBlock(true_block)
        self.visit(ctx.getChild(3))

        if not self.block_list[-1].is_terminated:
            self.builder_list[-1].branch(self.cur_endif_block)
        self.newBlock(false_block)
        self.symbol_table.func_quit()

    def visitElseconditionblock(self, ctx: MaverickParser.ElseconditionblockContext):
        self.symbol_table.func_enter()
        self.visit(ctx.getChild(1))
        self.symbol_table.func_quit()

    def visitBreak(self, ctx: MaverickParser.BreakContext):
        target_block = self.ctr_end_list[-1]
        self.builder_list[-1].branch(target_block)

    def visitContinue(self, ctx: MaverickParser.ContinueContext):
        target_block = self.ctr_cond_list[-1]
        self.builder_list[-1].branch(target_block)

    def visitCondition(self, ctx: MaverickParser.ConditionContext):
        return self.value2Boolean(self.visit(ctx.getChild(0)), False)

    def visitOr_expr(self, ctx: MaverickParser.Or_exprContext):
        # or
        expr_left = self.value2Boolean(self.visit(ctx.getChild(0)), False)
        expr_right = self.value2Boolean(self.visit(ctx.getChild(2)), False)
        builder = self.builder_list[-1]
        return {
            'type': expr_left['type'],
            'const': False,
            'name': builder.or_(expr_left['name'], expr_right['name'])
        }

    def visitAnd_expr(self, ctx: MaverickParser.And_exprContext):
        # and
        expr_left = self.value2Boolean(self.visit(ctx.getChild(0)), False)
        expr_right = self.value2Boolean(self.visit(ctx.getChild(2)), False)
        builder = self.builder_list[-1]
        return {
            'type': expr_left['type'],
            'const': False,
            'name': builder.and_(expr_left['name'], expr_right['name'])
        }

    def visitComp_expr(self, ctx: MaverickParser.Comp_exprContext):
        # comparison '<' | '>' | '<=' | '>=' | '!=' | '==';
        expr_left, expr_right = self.exprConvert(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        builder = self.builder_list[-1]
        operator = ctx.getChild(1).getText()
        return {
            'type': expr_left['type'],
            'const': False,
            'name': builder.icmp_signed(operator, expr_left['name'], expr_right['name'])
        }

    def visitExplist(self, ctx: MaverickParser.ExplistContext):
        exp_length = int((ctx.getChildCount() - 1) / 2 + 1)
        explist = []
        for i in range(0, exp_length, 1):
            explist.append(self.visit(ctx.getChild(2 * i)))
        return explist

    def visitNil_expr(self, ctx: MaverickParser.Nil_exprContext):
        return {
            'type': void,
            'const': False,
            'name': ir.Constant(void, None)
        }

    def visitTruefalse_expr(self, ctx: MaverickParser.Truefalse_exprContext):
        if ctx.getChild(0).getText() == 'false':
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

    def visitMuldivmod_expr(self, ctx: MaverickParser.Muldivmod_exprContext):
        builder = self.builder_list[-1]
        expr1, expr2, return_dict = self.get_return_dict(ctx)
        operator = ctx.getChild(1).getText()
        if operator == '*':
            return_dict["name"] = builder.mul(expr1['name'], expr2['name'])
        elif operator == '/':
            return_dict["name"] = builder.sdiv(expr1['name'], expr2['name'])
        elif operator == '%':
            return_dict["name"] = builder.srem(expr1['name'], expr2['name'])
        return return_dict

    def visitAddsub_expr(self, ctx: MaverickParser.Addsub_exprContext):
        builder = self.builder_list[-1]
        expr_left, expr_right, return_dict = self.get_return_dict(ctx)
        operator = ctx.getChild(1).getText()
        if operator == '+':
            return_dict["name"] = builder.add(expr_left['name'], expr_right['name'])
        elif operator == '-':
            return_dict["name"] = builder.sub(expr_left['name'], expr_right['name'])
        return return_dict

    def visitBitwise_expr(self, ctx: MaverickParser.Bitwise_exprContext):
        builder = self.builder_list[-1]
        expr1, expr2, return_dict = self.get_return_dict(ctx)
        operator = ctx.getChild(1).getText()
        if operator == '&':
            return_dict["name"] = builder.and_(expr1['name'], expr2['name'])
        elif operator == '|':
            return_dict["name"] = builder.or_(expr1['name'], expr2['name'])
        if operator == '~':
            return_dict["name"] = builder.xor(expr1['name'], expr2['name'])
        elif operator == '<<':
            return_dict["name"] = builder.shl(expr1['name'], expr2['name'])
        if operator == '>>':
            return_dict["name"] = builder.lshr(expr1['name'], expr2['name'])
        return return_dict

    def visitVar(self, ctx: MaverickParser.VarContext):
        id = ctx.getText()
        if self.func_list.get(id) is not None:
            return {
                'name': id
            }
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
                'type': void,
                'const': False,
                'name': ir.Constant(void, None)
            }

    def visitLaststat(self, ctx: MaverickParser.LaststatContext):
        if ctx.getChild(0).getText() == 'return':
            if (ctx.getChildCount() == 1):
                ret = self.builder_list[-1].ret_void()
            else:
                explist = self.visit(ctx.getChild(1))
                ret = self.builder_list[-1].ret(explist['name'])
            return {
                'type': void,
                'const': False,
                'name': ret
            }
        elif ctx.getChild(0).getText() == 'break':
            self.visit(ctx.getChild(0))
        elif ctx.getChild(0).getText() == 'continue':
            self.visit(ctx.getChild(0))

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

    def visitSelffunctioncall(self, ctx: MaverickParser.SelffunctioncallContext):
        func_name = self.visit(ctx.getChild(0))['name']
        func = self.func_list[func_name]
        args = self.visit(ctx.getChild(1))
        builder = self.builder_list[-1]
        arg_list = []
        for arg in args:
            arg_list.append(arg['name'])
        return {
            'type': func.function_type.return_type,
            'name': builder.call(func, arg_list)
        }

    def visitVarOrExp(self, ctx: MaverickParser.VarOrExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return self.visit(ctx.getChild(1))

    def visitNameAndArgs(self, ctx: MaverickParser.NameAndArgsContext):
        if ctx.getChild(0).getText() != ':':
            return self.visit(ctx.getChild(0))

    def visitArgs(self, ctx: MaverickParser.ArgsContext):
        if ctx.getChild(0).getText() == '(':
            if ctx.getChild(1).getText() == ')':
                return []
            else:
                return self.visit(ctx.getChild(1))

    def visitPrintfFunction(self, ctx: MaverickParser.PrintfFunctionContext):
        printf = self.func_list['printf']
        builder = self.builder_list[-1]
        zero = ir.Constant(int32, 0)
        arg_list = [builder.gep(self.visit(ctx.getChild(2))['name'], [zero, zero], inbounds=True)]
        length = ctx.getChildCount()
        for i in range(4, length - 1, 2):
            var_expr = self.visit(ctx.getChild(i))
            arg_list.append(var_expr['name'])
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
