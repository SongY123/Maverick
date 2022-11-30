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


    # Enter a parse tree produced by MaverickParser#funcdef.
    def enterFuncdef(self, ctx:MaverickParser.FuncdefContext):
        pass

    # Exit a parse tree produced by MaverickParser#funcdef.
    def exitFuncdef(self, ctx:MaverickParser.FuncdefContext):
        pass


    # Enter a parse tree produced by MaverickParser#localfuncdef.
    def enterLocalfuncdef(self, ctx:MaverickParser.LocalfuncdefContext):
        pass

    # Exit a parse tree produced by MaverickParser#localfuncdef.
    def exitLocalfuncdef(self, ctx:MaverickParser.LocalfuncdefContext):
        pass


    # Enter a parse tree produced by MaverickParser#attnamelist.
    def enterAttnamelist(self, ctx:MaverickParser.AttnamelistContext):
        pass

    # Exit a parse tree produced by MaverickParser#attnamelist.
    def exitAttnamelist(self, ctx:MaverickParser.AttnamelistContext):
        pass


    # Enter a parse tree produced by MaverickParser#attrib.
    def enterAttrib(self, ctx:MaverickParser.AttribContext):
        pass

    # Exit a parse tree produced by MaverickParser#attrib.
    def exitAttrib(self, ctx:MaverickParser.AttribContext):
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


    # Enter a parse tree produced by MaverickParser#exp.
    def enterExp(self, ctx:MaverickParser.ExpContext):
        pass

    # Exit a parse tree produced by MaverickParser#exp.
    def exitExp(self, ctx:MaverickParser.ExpContext):
        pass


    # Enter a parse tree produced by MaverickParser#prefixexp.
    def enterPrefixexp(self, ctx:MaverickParser.PrefixexpContext):
        pass

    # Exit a parse tree produced by MaverickParser#prefixexp.
    def exitPrefixexp(self, ctx:MaverickParser.PrefixexpContext):
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


    # Enter a parse tree produced by MaverickParser#functiondef.
    def enterFunctiondef(self, ctx:MaverickParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by MaverickParser#functiondef.
    def exitFunctiondef(self, ctx:MaverickParser.FunctiondefContext):
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



del MaverickParser