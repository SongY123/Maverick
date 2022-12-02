# Generated from /Users/songyang/Desktop/buaa/课程/程序设计语言/Maverick/antlr/Maverick.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MaverickParser import MaverickParser
else:
    from MaverickParser import MaverickParser

# This class defines a complete generic visitor for a parse tree produced by MaverickParser.

class MaverickVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MaverickParser#chunk.
    def visitChunk(self, ctx:MaverickParser.ChunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#block.
    def visitBlock(self, ctx:MaverickParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#stat.
    def visitStat(self, ctx:MaverickParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#varinit.
    def visitVarinit(self, ctx:MaverickParser.VarinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#varassign.
    def visitVarassign(self, ctx:MaverickParser.VarassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#whileblock.
    def visitWhileblock(self, ctx:MaverickParser.WhileblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#repeatblock.
    def visitRepeatblock(self, ctx:MaverickParser.RepeatblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#ifblock.
    def visitIfblock(self, ctx:MaverickParser.IfblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#ifconditionblock.
    def visitIfconditionblock(self, ctx:MaverickParser.IfconditionblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#elseifconditionblock.
    def visitElseifconditionblock(self, ctx:MaverickParser.ElseifconditionblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#elseconditionblock.
    def visitElseconditionblock(self, ctx:MaverickParser.ElseconditionblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#forblock.
    def visitForblock(self, ctx:MaverickParser.ForblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#funcdef.
    def visitFuncdef(self, ctx:MaverickParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#laststat.
    def visitLaststat(self, ctx:MaverickParser.LaststatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#label.
    def visitLabel(self, ctx:MaverickParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#funcname.
    def visitFuncname(self, ctx:MaverickParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#varlist.
    def visitVarlist(self, ctx:MaverickParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#namelist.
    def visitNamelist(self, ctx:MaverickParser.NamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#explist.
    def visitExplist(self, ctx:MaverickParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#condition.
    def visitCondition(self, ctx:MaverickParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#tableconstructor_expr.
    def visitTableconstructor_expr(self, ctx:MaverickParser.Tableconstructor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#strcat_expr.
    def visitStrcat_expr(self, ctx:MaverickParser.Strcat_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#nil_expr.
    def visitNil_expr(self, ctx:MaverickParser.Nil_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#functioncall_expr.
    def visitFunctioncall_expr(self, ctx:MaverickParser.Functioncall_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#varorexp_expr.
    def visitVarorexp_expr(self, ctx:MaverickParser.Varorexp_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#comp_expr.
    def visitComp_expr(self, ctx:MaverickParser.Comp_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#addsub_expr.
    def visitAddsub_expr(self, ctx:MaverickParser.Addsub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#power_expr.
    def visitPower_expr(self, ctx:MaverickParser.Power_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#more_expr.
    def visitMore_expr(self, ctx:MaverickParser.More_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#string_expr.
    def visitString_expr(self, ctx:MaverickParser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#unary_expr.
    def visitUnary_expr(self, ctx:MaverickParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#bitwise_expr.
    def visitBitwise_expr(self, ctx:MaverickParser.Bitwise_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#and_expr.
    def visitAnd_expr(self, ctx:MaverickParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#or_expr.
    def visitOr_expr(self, ctx:MaverickParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#muldivmod_expr.
    def visitMuldivmod_expr(self, ctx:MaverickParser.Muldivmod_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#truefalse_expr.
    def visitTruefalse_expr(self, ctx:MaverickParser.Truefalse_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#number_expr.
    def visitNumber_expr(self, ctx:MaverickParser.Number_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#functioncall.
    def visitFunctioncall(self, ctx:MaverickParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#varOrExp.
    def visitVarOrExp(self, ctx:MaverickParser.VarOrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#var.
    def visitVar(self, ctx:MaverickParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#varSuffix.
    def visitVarSuffix(self, ctx:MaverickParser.VarSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#nameAndArgs.
    def visitNameAndArgs(self, ctx:MaverickParser.NameAndArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#args.
    def visitArgs(self, ctx:MaverickParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#funcbody.
    def visitFuncbody(self, ctx:MaverickParser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#parlist.
    def visitParlist(self, ctx:MaverickParser.ParlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#tableconstructor.
    def visitTableconstructor(self, ctx:MaverickParser.TableconstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#fieldlist.
    def visitFieldlist(self, ctx:MaverickParser.FieldlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#field.
    def visitField(self, ctx:MaverickParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#fieldsep.
    def visitFieldsep(self, ctx:MaverickParser.FieldsepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorOr.
    def visitOperatorOr(self, ctx:MaverickParser.OperatorOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorAnd.
    def visitOperatorAnd(self, ctx:MaverickParser.OperatorAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorComparison.
    def visitOperatorComparison(self, ctx:MaverickParser.OperatorComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorStrcat.
    def visitOperatorStrcat(self, ctx:MaverickParser.OperatorStrcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorAddSub.
    def visitOperatorAddSub(self, ctx:MaverickParser.OperatorAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorMulDivMod.
    def visitOperatorMulDivMod(self, ctx:MaverickParser.OperatorMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorBitwise.
    def visitOperatorBitwise(self, ctx:MaverickParser.OperatorBitwiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorUnary.
    def visitOperatorUnary(self, ctx:MaverickParser.OperatorUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#operatorPower.
    def visitOperatorPower(self, ctx:MaverickParser.OperatorPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#number.
    def visitNumber(self, ctx:MaverickParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#string.
    def visitString(self, ctx:MaverickParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#type.
    def visitType(self, ctx:MaverickParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#myINT.
    def visitMyINT(self, ctx:MaverickParser.MyINTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#myHEX.
    def visitMyHEX(self, ctx:MaverickParser.MyHEXContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#myFLOAT.
    def visitMyFLOAT(self, ctx:MaverickParser.MyFLOATContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#break.
    def visitBreak(self, ctx:MaverickParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#continue.
    def visitContinue(self, ctx:MaverickParser.ContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#printfFunction.
    def visitPrintfFunction(self, ctx:MaverickParser.PrintfFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#scanfFunction.
    def visitScanfFunction(self, ctx:MaverickParser.ScanfFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#selffunctioncall.
    def visitSelffunctioncall(self, ctx:MaverickParser.SelffunctioncallContext):
        return self.visitChildren(ctx)



del MaverickParser