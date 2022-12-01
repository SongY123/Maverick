# Generated from /Users/songyang/Desktop/buaa/课程/程序设计语言/Maverick/antlr/Maverick.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MaverickParser import MaverickParser
else:
    from MaverickParser import MaverickParser

# This class defines a complete listener for a parse tree produced by MaverickParser.
class MaverickListener(ParseTreeListener):

    # Enter a parse tree produced by MaverickParser#chunk.
    def enterChunk(self, ctx:MaverickParser.ChunkContext):
        pass

    # Exit a parse tree produced by MaverickParser#chunk.
    def exitChunk(self, ctx:MaverickParser.ChunkContext):
        pass


    # Enter a parse tree produced by MaverickParser#block.
    def enterBlock(self, ctx:MaverickParser.BlockContext):
        pass

    # Exit a parse tree produced by MaverickParser#block.
    def exitBlock(self, ctx:MaverickParser.BlockContext):
        pass


    # Enter a parse tree produced by MaverickParser#stat.
    def enterStat(self, ctx:MaverickParser.StatContext):
        pass

    # Exit a parse tree produced by MaverickParser#stat.
    def exitStat(self, ctx:MaverickParser.StatContext):
        pass


    # Enter a parse tree produced by MaverickParser#varinit.
    def enterVarinit(self, ctx:MaverickParser.VarinitContext):
        pass

    # Exit a parse tree produced by MaverickParser#varinit.
    def exitVarinit(self, ctx:MaverickParser.VarinitContext):
        pass


    # Enter a parse tree produced by MaverickParser#varassign.
    def enterVarassign(self, ctx:MaverickParser.VarassignContext):
        pass

    # Exit a parse tree produced by MaverickParser#varassign.
    def exitVarassign(self, ctx:MaverickParser.VarassignContext):
        pass


    # Enter a parse tree produced by MaverickParser#whileblock.
    def enterWhileblock(self, ctx:MaverickParser.WhileblockContext):
        pass

    # Exit a parse tree produced by MaverickParser#whileblock.
    def exitWhileblock(self, ctx:MaverickParser.WhileblockContext):
        pass


    # Enter a parse tree produced by MaverickParser#repeatblock.
    def enterRepeatblock(self, ctx:MaverickParser.RepeatblockContext):
        pass

    # Exit a parse tree produced by MaverickParser#repeatblock.
    def exitRepeatblock(self, ctx:MaverickParser.RepeatblockContext):
        pass


    # Enter a parse tree produced by MaverickParser#ifblock.
    def enterIfblock(self, ctx:MaverickParser.IfblockContext):
        pass

    # Exit a parse tree produced by MaverickParser#ifblock.
    def exitIfblock(self, ctx:MaverickParser.IfblockContext):
        pass


    # Enter a parse tree produced by MaverickParser#ifconditionblock.
    def enterIfconditionblock(self, ctx:MaverickParser.IfconditionblockContext):
        pass

    # Exit a parse tree produced by MaverickParser#ifconditionblock.
    def exitIfconditionblock(self, ctx:MaverickParser.IfconditionblockContext):
        pass


    # Enter a parse tree produced by MaverickParser#elseifconditionblock.
    def enterElseifconditionblock(self, ctx:MaverickParser.ElseifconditionblockContext):
        pass

    # Exit a parse tree produced by MaverickParser#elseifconditionblock.
    def exitElseifconditionblock(self, ctx:MaverickParser.ElseifconditionblockContext):
        pass


    # Enter a parse tree produced by MaverickParser#elseconditionblock.
    def enterElseconditionblock(self, ctx:MaverickParser.ElseconditionblockContext):
        pass

    # Exit a parse tree produced by MaverickParser#elseconditionblock.
    def exitElseconditionblock(self, ctx:MaverickParser.ElseconditionblockContext):
        pass


    # Enter a parse tree produced by MaverickParser#forequalblock.
    def enterForequalblock(self, ctx:MaverickParser.ForequalblockContext):
        pass

    # Exit a parse tree produced by MaverickParser#forequalblock.
    def exitForequalblock(self, ctx:MaverickParser.ForequalblockContext):
        pass


    # Enter a parse tree produced by MaverickParser#forinblock.
    def enterForinblock(self, ctx:MaverickParser.ForinblockContext):
        pass

    # Exit a parse tree produced by MaverickParser#forinblock.
    def exitForinblock(self, ctx:MaverickParser.ForinblockContext):
        pass


    # Enter a parse tree produced by MaverickParser#funcdef.
    def enterFuncdef(self, ctx:MaverickParser.FuncdefContext):
        pass

    # Exit a parse tree produced by MaverickParser#funcdef.
    def exitFuncdef(self, ctx:MaverickParser.FuncdefContext):
        pass


    # Enter a parse tree produced by MaverickParser#laststat.
    def enterLaststat(self, ctx:MaverickParser.LaststatContext):
        pass

    # Exit a parse tree produced by MaverickParser#laststat.
    def exitLaststat(self, ctx:MaverickParser.LaststatContext):
        pass


    # Enter a parse tree produced by MaverickParser#label.
    def enterLabel(self, ctx:MaverickParser.LabelContext):
        pass

    # Exit a parse tree produced by MaverickParser#label.
    def exitLabel(self, ctx:MaverickParser.LabelContext):
        pass


    # Enter a parse tree produced by MaverickParser#funcname.
    def enterFuncname(self, ctx:MaverickParser.FuncnameContext):
        pass

    # Exit a parse tree produced by MaverickParser#funcname.
    def exitFuncname(self, ctx:MaverickParser.FuncnameContext):
        pass


    # Enter a parse tree produced by MaverickParser#varlist.
    def enterVarlist(self, ctx:MaverickParser.VarlistContext):
        pass

    # Exit a parse tree produced by MaverickParser#varlist.
    def exitVarlist(self, ctx:MaverickParser.VarlistContext):
        pass


    # Enter a parse tree produced by MaverickParser#namelist.
    def enterNamelist(self, ctx:MaverickParser.NamelistContext):
        pass

    # Exit a parse tree produced by MaverickParser#namelist.
    def exitNamelist(self, ctx:MaverickParser.NamelistContext):
        pass


    # Enter a parse tree produced by MaverickParser#explist.
    def enterExplist(self, ctx:MaverickParser.ExplistContext):
        pass

    # Exit a parse tree produced by MaverickParser#explist.
    def exitExplist(self, ctx:MaverickParser.ExplistContext):
        pass


    # Enter a parse tree produced by MaverickParser#condition.
    def enterCondition(self, ctx:MaverickParser.ConditionContext):
        pass

    # Exit a parse tree produced by MaverickParser#condition.
    def exitCondition(self, ctx:MaverickParser.ConditionContext):
        pass


    # Enter a parse tree produced by MaverickParser#tableconstructor_expr.
    def enterTableconstructor_expr(self, ctx:MaverickParser.Tableconstructor_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#tableconstructor_expr.
    def exitTableconstructor_expr(self, ctx:MaverickParser.Tableconstructor_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#strcat_expr.
    def enterStrcat_expr(self, ctx:MaverickParser.Strcat_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#strcat_expr.
    def exitStrcat_expr(self, ctx:MaverickParser.Strcat_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#nil_expr.
    def enterNil_expr(self, ctx:MaverickParser.Nil_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#nil_expr.
    def exitNil_expr(self, ctx:MaverickParser.Nil_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#functioncall_expr.
    def enterFunctioncall_expr(self, ctx:MaverickParser.Functioncall_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#functioncall_expr.
    def exitFunctioncall_expr(self, ctx:MaverickParser.Functioncall_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#varorexp_expr.
    def enterVarorexp_expr(self, ctx:MaverickParser.Varorexp_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#varorexp_expr.
    def exitVarorexp_expr(self, ctx:MaverickParser.Varorexp_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#comp_expr.
    def enterComp_expr(self, ctx:MaverickParser.Comp_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#comp_expr.
    def exitComp_expr(self, ctx:MaverickParser.Comp_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#addsub_expr.
    def enterAddsub_expr(self, ctx:MaverickParser.Addsub_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#addsub_expr.
    def exitAddsub_expr(self, ctx:MaverickParser.Addsub_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#power_expr.
    def enterPower_expr(self, ctx:MaverickParser.Power_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#power_expr.
    def exitPower_expr(self, ctx:MaverickParser.Power_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#more_expr.
    def enterMore_expr(self, ctx:MaverickParser.More_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#more_expr.
    def exitMore_expr(self, ctx:MaverickParser.More_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#string_expr.
    def enterString_expr(self, ctx:MaverickParser.String_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#string_expr.
    def exitString_expr(self, ctx:MaverickParser.String_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#unary_expr.
    def enterUnary_expr(self, ctx:MaverickParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#unary_expr.
    def exitUnary_expr(self, ctx:MaverickParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#bitwise_expr.
    def enterBitwise_expr(self, ctx:MaverickParser.Bitwise_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#bitwise_expr.
    def exitBitwise_expr(self, ctx:MaverickParser.Bitwise_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#and_expr.
    def enterAnd_expr(self, ctx:MaverickParser.And_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#and_expr.
    def exitAnd_expr(self, ctx:MaverickParser.And_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#or_expr.
    def enterOr_expr(self, ctx:MaverickParser.Or_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#or_expr.
    def exitOr_expr(self, ctx:MaverickParser.Or_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#muldivmod_expr.
    def enterMuldivmod_expr(self, ctx:MaverickParser.Muldivmod_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#muldivmod_expr.
    def exitMuldivmod_expr(self, ctx:MaverickParser.Muldivmod_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#truefalse_expr.
    def enterTruefalse_expr(self, ctx:MaverickParser.Truefalse_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#truefalse_expr.
    def exitTruefalse_expr(self, ctx:MaverickParser.Truefalse_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#number_expr.
    def enterNumber_expr(self, ctx:MaverickParser.Number_exprContext):
        pass

    # Exit a parse tree produced by MaverickParser#number_expr.
    def exitNumber_expr(self, ctx:MaverickParser.Number_exprContext):
        pass


    # Enter a parse tree produced by MaverickParser#functioncall.
    def enterFunctioncall(self, ctx:MaverickParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by MaverickParser#functioncall.
    def exitFunctioncall(self, ctx:MaverickParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by MaverickParser#varOrExp.
    def enterVarOrExp(self, ctx:MaverickParser.VarOrExpContext):
        pass

    # Exit a parse tree produced by MaverickParser#varOrExp.
    def exitVarOrExp(self, ctx:MaverickParser.VarOrExpContext):
        pass


    # Enter a parse tree produced by MaverickParser#var.
    def enterVar(self, ctx:MaverickParser.VarContext):
        pass

    # Exit a parse tree produced by MaverickParser#var.
    def exitVar(self, ctx:MaverickParser.VarContext):
        pass


    # Enter a parse tree produced by MaverickParser#varSuffix.
    def enterVarSuffix(self, ctx:MaverickParser.VarSuffixContext):
        pass

    # Exit a parse tree produced by MaverickParser#varSuffix.
    def exitVarSuffix(self, ctx:MaverickParser.VarSuffixContext):
        pass


    # Enter a parse tree produced by MaverickParser#nameAndArgs.
    def enterNameAndArgs(self, ctx:MaverickParser.NameAndArgsContext):
        pass

    # Exit a parse tree produced by MaverickParser#nameAndArgs.
    def exitNameAndArgs(self, ctx:MaverickParser.NameAndArgsContext):
        pass


    # Enter a parse tree produced by MaverickParser#args.
    def enterArgs(self, ctx:MaverickParser.ArgsContext):
        pass

    # Exit a parse tree produced by MaverickParser#args.
    def exitArgs(self, ctx:MaverickParser.ArgsContext):
        pass


    # Enter a parse tree produced by MaverickParser#funcbody.
    def enterFuncbody(self, ctx:MaverickParser.FuncbodyContext):
        pass

    # Exit a parse tree produced by MaverickParser#funcbody.
    def exitFuncbody(self, ctx:MaverickParser.FuncbodyContext):
        pass


    # Enter a parse tree produced by MaverickParser#parlist.
    def enterParlist(self, ctx:MaverickParser.ParlistContext):
        pass

    # Exit a parse tree produced by MaverickParser#parlist.
    def exitParlist(self, ctx:MaverickParser.ParlistContext):
        pass


    # Enter a parse tree produced by MaverickParser#tableconstructor.
    def enterTableconstructor(self, ctx:MaverickParser.TableconstructorContext):
        pass

    # Exit a parse tree produced by MaverickParser#tableconstructor.
    def exitTableconstructor(self, ctx:MaverickParser.TableconstructorContext):
        pass


    # Enter a parse tree produced by MaverickParser#fieldlist.
    def enterFieldlist(self, ctx:MaverickParser.FieldlistContext):
        pass

    # Exit a parse tree produced by MaverickParser#fieldlist.
    def exitFieldlist(self, ctx:MaverickParser.FieldlistContext):
        pass


    # Enter a parse tree produced by MaverickParser#field.
    def enterField(self, ctx:MaverickParser.FieldContext):
        pass

    # Exit a parse tree produced by MaverickParser#field.
    def exitField(self, ctx:MaverickParser.FieldContext):
        pass


    # Enter a parse tree produced by MaverickParser#fieldsep.
    def enterFieldsep(self, ctx:MaverickParser.FieldsepContext):
        pass

    # Exit a parse tree produced by MaverickParser#fieldsep.
    def exitFieldsep(self, ctx:MaverickParser.FieldsepContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorOr.
    def enterOperatorOr(self, ctx:MaverickParser.OperatorOrContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorOr.
    def exitOperatorOr(self, ctx:MaverickParser.OperatorOrContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorAnd.
    def enterOperatorAnd(self, ctx:MaverickParser.OperatorAndContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorAnd.
    def exitOperatorAnd(self, ctx:MaverickParser.OperatorAndContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorComparison.
    def enterOperatorComparison(self, ctx:MaverickParser.OperatorComparisonContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorComparison.
    def exitOperatorComparison(self, ctx:MaverickParser.OperatorComparisonContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorStrcat.
    def enterOperatorStrcat(self, ctx:MaverickParser.OperatorStrcatContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorStrcat.
    def exitOperatorStrcat(self, ctx:MaverickParser.OperatorStrcatContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorAddSub.
    def enterOperatorAddSub(self, ctx:MaverickParser.OperatorAddSubContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorAddSub.
    def exitOperatorAddSub(self, ctx:MaverickParser.OperatorAddSubContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorMulDivMod.
    def enterOperatorMulDivMod(self, ctx:MaverickParser.OperatorMulDivModContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorMulDivMod.
    def exitOperatorMulDivMod(self, ctx:MaverickParser.OperatorMulDivModContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorBitwise.
    def enterOperatorBitwise(self, ctx:MaverickParser.OperatorBitwiseContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorBitwise.
    def exitOperatorBitwise(self, ctx:MaverickParser.OperatorBitwiseContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorUnary.
    def enterOperatorUnary(self, ctx:MaverickParser.OperatorUnaryContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorUnary.
    def exitOperatorUnary(self, ctx:MaverickParser.OperatorUnaryContext):
        pass


    # Enter a parse tree produced by MaverickParser#operatorPower.
    def enterOperatorPower(self, ctx:MaverickParser.OperatorPowerContext):
        pass

    # Exit a parse tree produced by MaverickParser#operatorPower.
    def exitOperatorPower(self, ctx:MaverickParser.OperatorPowerContext):
        pass


    # Enter a parse tree produced by MaverickParser#number.
    def enterNumber(self, ctx:MaverickParser.NumberContext):
        pass

    # Exit a parse tree produced by MaverickParser#number.
    def exitNumber(self, ctx:MaverickParser.NumberContext):
        pass


    # Enter a parse tree produced by MaverickParser#string.
    def enterString(self, ctx:MaverickParser.StringContext):
        pass

    # Exit a parse tree produced by MaverickParser#string.
    def exitString(self, ctx:MaverickParser.StringContext):
        pass


    # Enter a parse tree produced by MaverickParser#type.
    def enterType(self, ctx:MaverickParser.TypeContext):
        pass

    # Exit a parse tree produced by MaverickParser#type.
    def exitType(self, ctx:MaverickParser.TypeContext):
        pass


    # Enter a parse tree produced by MaverickParser#myINT.
    def enterMyINT(self, ctx:MaverickParser.MyINTContext):
        pass

    # Exit a parse tree produced by MaverickParser#myINT.
    def exitMyINT(self, ctx:MaverickParser.MyINTContext):
        pass


    # Enter a parse tree produced by MaverickParser#myHEX.
    def enterMyHEX(self, ctx:MaverickParser.MyHEXContext):
        pass

    # Exit a parse tree produced by MaverickParser#myHEX.
    def exitMyHEX(self, ctx:MaverickParser.MyHEXContext):
        pass


    # Enter a parse tree produced by MaverickParser#myFLOAT.
    def enterMyFLOAT(self, ctx:MaverickParser.MyFLOATContext):
        pass

    # Exit a parse tree produced by MaverickParser#myFLOAT.
    def exitMyFLOAT(self, ctx:MaverickParser.MyFLOATContext):
        pass


    # Enter a parse tree produced by MaverickParser#break.
    def enterBreak(self, ctx:MaverickParser.BreakContext):
        pass

    # Exit a parse tree produced by MaverickParser#break.
    def exitBreak(self, ctx:MaverickParser.BreakContext):
        pass


    # Enter a parse tree produced by MaverickParser#continue.
    def enterContinue(self, ctx:MaverickParser.ContinueContext):
        pass

    # Exit a parse tree produced by MaverickParser#continue.
    def exitContinue(self, ctx:MaverickParser.ContinueContext):
        pass


    # Enter a parse tree produced by MaverickParser#printfFunction.
    def enterPrintfFunction(self, ctx:MaverickParser.PrintfFunctionContext):
        pass

    # Exit a parse tree produced by MaverickParser#printfFunction.
    def exitPrintfFunction(self, ctx:MaverickParser.PrintfFunctionContext):
        pass


    # Enter a parse tree produced by MaverickParser#scanfFunction.
    def enterScanfFunction(self, ctx:MaverickParser.ScanfFunctionContext):
        pass

    # Exit a parse tree produced by MaverickParser#scanfFunction.
    def exitScanfFunction(self, ctx:MaverickParser.ScanfFunctionContext):
        pass


    # Enter a parse tree produced by MaverickParser#selffunctioncall.
    def enterSelffunctioncall(self, ctx:MaverickParser.SelffunctioncallContext):
        pass

    # Exit a parse tree produced by MaverickParser#selffunctioncall.
    def exitSelffunctioncall(self, ctx:MaverickParser.SelffunctioncallContext):
        pass



del MaverickParser