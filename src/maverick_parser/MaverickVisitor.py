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


    # Visit a parse tree produced by MaverickParser#funcdef.
    def visitFuncdef(self, ctx:MaverickParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#attrib.
    def visitAttrib(self, ctx:MaverickParser.AttribContext):
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


    # Visit a parse tree produced by MaverickParser#exp.
    def visitExp(self, ctx:MaverickParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#prefixexp.
    def visitPrefixexp(self, ctx:MaverickParser.PrefixexpContext):
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


    # Visit a parse tree produced by MaverickParser#printfFunction.
    def visitPrintfFunction(self, ctx:MaverickParser.PrintfFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MaverickParser#scanfFunction.
    def visitScanfFunction(self, ctx:MaverickParser.ScanfFunctionContext):
        return self.visitChildren(ctx)



del MaverickParser