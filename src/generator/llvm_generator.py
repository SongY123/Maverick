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

        # used to store class info
        # "classname": {fiel_dict: {"name" : type}, func_dict: {"name" : ir.Function}
        self.class_dict = dict()
        # tell visitfuncdef if we need to pass this pointer to function
        self.this_class_name = None
        self.this_func_name = None
        self.need_load = True
        self.function_call = False

        self.constants = 0

        func_name = 'main'
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

    def exprConvert(self, expr_left, expr_right):
        if expr_left['type'] == expr_right['type']:
            return expr_left, expr_right
        else:
            raise TypeMisatchException(expr_left, expr_right)

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

    def visitNewclass(self, ctx: MaverickParser.NewclassContext):
        classname = ctx.getChild(0).getText()
        varname = ctx.getChild(1).getText()
        var = self.builder_list[-1].alloca(self.class_dict[classname]["named_class"], name=varname)
        self.symbol_table.insert_item(varname, {'Type': self.class_dict[classname]["named_class"],
                'Name': var})

        return var


    def visitDeleteclass(self, ctx: MaverickParser.DeleteclassContext):
        return super().visitDeleteclass(ctx)

    def visitClassconstructor(self, ctx: MaverickParser.ClassconstructorContext):
        classname = ctx.getChild(1).getText()

        # visit field
        if self.class_dict.get(classname) is not None:
            raise ClassNameDuplicateException(classname)
        field_dict = self.visit(ctx.getChild(2))

        # class_ = ClassType.construct(classname, field_dict)
        llvm_class = ir.LiteralStructType([value for value in field_dict.values()])
        named_class = self.module.context.get_identified_type(classname)
        named_class.packed = True
        named_class.set_body(*llvm_class)
        self.class_dict[classname] = {
            "field_dict": field_dict,
            "named_class": named_class
        }

        # TODO create default constructor

        # visit class function
        self.this_class_name = classname
        func_dict = self.visit(ctx.getChild(3))
        self.this_class_name = None


    def visitClassfieldlist(self, ctx: MaverickParser.ClassfieldlistContext):
        field_dict = dict()
        for i in range(ctx.getChildCount()):
            field = self.visit(ctx.getChild(i))
            field_dict[field["Name"]] = field["Type"]
        return field_dict

    def visitField(self, ctx: MaverickParser.FieldContext):
        var_type = self.visitType(ctx.getChild(0))
        var_id = ctx.getChild(1).getText()
        if ctx.getChildCount() == 4:
            val = self.visit(ctx.getChild(3))
        return {
            "Type": var_type,
            "Name": var_id
        }

    def visitClassfunclist(self, ctx: MaverickParser.ClassfunclistContext):
        return super().visitClassfunclist(ctx)


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
        if ctx.getText() == 'char':
            return char
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
                raise VariableInitializationException(id)

    def visitArrayinit(self, ctx: MaverickParser.ArrayinitContext):
        type = self.visit(ctx.getChild(0))
        id = ctx.getChild(1).getText()
        length = int(ctx.getChild(3).getText())
        if self.symbol_table.is_global() == True:
            mvar = ir.GlobalVariable(self.module, ir.ArrayType(type, length), name=id)
            mvar.linkage = 'internal'
        else:
            mvar = self.builder_list[-1].alloca(ir.ArrayType(type, length), name=id)
        self.symbol_table.insert_item(id, {'Type': ir.ArrayType(type, length), 'Name': mvar})
        return

    def visitArrayitem(self, ctx: MaverickParser.ArrayitemContext):
        require_load = self.need_load
        self.need_load = False
        res = self.visit(ctx.getChild(0))
        self.need_load = require_load

        if isinstance(res['type'], ir.types.ArrayType):
            builder = self.builder_list[-1]
            require_load = self.need_load
            self.need_load = True
            index = self.visit(ctx.getChild(2))  # subscript
            self.need_load = require_load
            return_dict = {
                'type': res['type'].element,
                'const': False
            }
            zero = ir.Constant(int32, 0)
            return_dict["name"] = builder.gep(res['name'], [zero, index['name']], inbounds=True)
            if self.need_load:
                return_dict["name"] = builder.load(return_dict["name"])
            return return_dict
        else:
            print("类型错误:" + ctx.getText())
            exit(0)

    def visitVarassign(self, ctx: MaverickParser.VarassignContext):
        builder = self.builder_list[-1]
        val = self.visit(ctx.getChild(2))
        need_load_cache = self.need_load
        self.need_load = False
        zero = ir.Constant(int32, 0)
        if self.this_class_name is not None:
            offset = 0
            var_name = ctx.getChild(0).getText()
            for name, type in self.class_dict[self.this_class_name]['field_dict'].items():
                if name != var_name:
                    offset += 1
                else:
                    break
            var = {
                'type': int32,
                'const': False,
                'name': builder.gep(self.func_list[self.this_func_name].args[0], [zero, ir.Constant(type, offset)])
            }
            var["name"].type = ir.PointerType(self.class_dict[self.this_class_name]['field_dict'][var_name])
        else:
            var = self.visit(ctx.getChild(0))
        self.need_load = need_load_cache
        builder.store(val['name'], var['name'])
        return {'type': var['type'], 'name': builder.load(var['name'])}

    def visitFuncdef(self, ctx: MaverickParser.FuncdefContext):
        """
        funcdef: 'function' type funcname '(' parlist? ')' funcbody
        """
        if self.this_class_name is not None:
            func_name = self.this_class_name + '.' + ctx.getChild(2).getText()
        else:
            func_name = ctx.getChild(2).getText()
        self.this_func_name = func_name
        if func_name in self.func_list:
            raise FunctionNameDuplicateException(func_name)
        return_type = self.visit(ctx.getChild(1))
        # func params
        para_list = self.visit(ctx.getChild(4))
        if self.this_class_name is not None:
            para_list.insert(0, {
                "name": "this",
                "type": ir.PointerType(self.class_dict[self.this_class_name]["named_class"])}
                             )
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
        if self.this_class_name is not None:
            begin_i = 1
        else:
            begin_i = 0
        for i  in range(begin_i, len(para_list)):
            mvar = builder.alloca(para_list[i]['type'])
            builder.store(llvm_func.args[i], mvar)
            self.symbol_table.insert_item(para_list[i]['name'], {'Type': para_list[i]['type'], 'Name': mvar})
        self.visit(ctx.getChild(ctx.getChildCount() - 1))  # funcbody
        self.cur_func = ''
        self.block_list.pop()
        self.builder_list.pop()
        self.symbol_table.func_quit()
        self.this_func_name = None

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


    def visitForblock(self, ctx: MaverickParser.ForblockContext):
        """
        forblock
            : 'for' varassign ',' exp (',' exp)? 'do' block 'end'
            ;
        """
        self.symbol_table.func_enter()

        has_step = ctx.getChildCount() == 9

        var = self.visit(ctx.getChild(1))

        cur_builder = self.builder_list[-1]
        cond_block = cur_builder.append_basic_block()
        body_block = cur_builder.append_basic_block()
        endfor_block = cur_builder.append_basic_block()
        self.ctr_cond_list.append(cond_block)
        self.ctr_end_list.append(endfor_block)

        cur_builder.branch(cond_block)
        self.newBlock(cond_block)
        cur_builder = self.builder_list[-1]
        id = ctx.getChild(1).getChild(0).getText()
        item = self.symbol_table.get_item(id)
        if self.need_load:
            var = cur_builder.load(item["Name"])
        else:
            var = item["Name"]
        max_value = self.visit(ctx.getChild(3))

        cond = cur_builder.icmp_signed("<", var, max_value['name'])

        cur_builder.cbranch(cond, body_block, endfor_block)

        self.newBlock(body_block)
        cur_builder = self.builder_list[-1]
        # visit block
        if has_step:
            self.visit(ctx.getChild(7))
        else:
            self.visit(ctx.getChild(5))

        # visit step
        if has_step:
            val = self.visit(ctx.getChild(5))
            result = cur_builder.add(var, val['name'])
            # return {'type': var['type'], 'name': cur_builder.load(var['name'])}
        else:
            result = cur_builder.add(var, ir.Constant(int32, 1))
        item = self.symbol_table.get_item(id)["Name"]
        cur_builder.store(result, item)

        try:
            cur_builder.branch(cond_block)
        except AssertionError:
            print("Branch optimize")

        self.newBlock(endfor_block)
        self.ctr_cond_list.pop(-1)
        self.ctr_end_list.pop(-1)
        self.symbol_table.func_quit()

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
        zero = ir.Constant(int32, 0)
        if self.function_call:
            if self.func_list.get(id) is not None:
                return {
                    'name': id
                }
            else:
                var_name = id.split('.')[0]
                class_ = self.symbol_table.get_item(var_name)
                return {
                    'name': class_['Type'].name + '.' + id.split('.')[1]
                }
        if id.find('.') != -1:
            var_name = id.split('.')[0]
            mem_name= id.split('.')[1]
            class_ = self.symbol_table.get_item(var_name)
            offset = 0
            for name, type in self.class_dict[class_['Type'].name]['field_dict'].items():
                if name != mem_name:
                    offset += 1
                else:
                    mem_type = type
                    break
            return {
                'type': mem_type.as_pointer(),
                "const": False,
                'name': self.builder_list[-1].gep(self.symbol_table.get_item(var_name)['Name'], [zero, ir.Constant(mem_type, offset)])
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
        string : : NORMALSTRING | CHARSTRING;
        """
        if ctx.getText()[0] == '\'':
            # char
            return {
                'type': char,
                'const': True,
                'name': ir.Constant(char, ord(ctx.getText()[1]))
            }
        else:
            # string
            str = ctx.getText().replace('\\n', '\n')[1:-1] + '\0'
            length = len(bytearray(str, 'utf-8'))
            ret = ir.GlobalVariable(self.module, ir.ArrayType(byte, length), ".str%d" % self.
                                    constants)
            self.constants += 1
            ret.global_constant = True
            ret.initializer = ir.Constant(ir.ArrayType(byte, length), bytearray(str, 'utf-8'))
            return {
                'type': ir.ArrayType(byte, length),
                'const': False,
                'name': ret
            }

    def visitSelffunctioncall(self, ctx: MaverickParser.SelffunctioncallContext):
        self.function_call = True
        func_name = self.visit(ctx.getChild(0))['name']
        self.function_call = False
        func = self.func_list[func_name]
        args = self.visit(ctx.getChild(1))
        builder = self.builder_list[-1]
        arg_list = []
        if func_name.find('.') != -1:
            var_name = ctx.getChild(0).getText().split('.')[0]
            arg_list.append(self.symbol_table.get_item(var_name)['Name'])
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
            if var_expr['type'].is_pointer:
                var_expr['name'] = builder.load(var_expr['name'])
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

    tree = parser.chunk()
    v = MVisitor(triple, data_layout)
    v.visit(tree)
    v.builder_list[0].ret_void()
    v.save(output_filename)
