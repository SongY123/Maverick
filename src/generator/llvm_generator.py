from antlr4 import *
from llvmlite import ir

from maverick_parser.MaverickLexer import MaverickLexer
from maverick_parser.MaverickParser import MaverickParser
from maverick_parser.MaverickVisitor import MaverickVisitor


class MVisitor(MaverickVisitor):

    def __init__(self, triple, data_layout):
        super(MaverickVisitor, self).__init__()
        self.module = ir.Module()
        self.module.triple = triple
        self.module.data_layout = data_layout

    def save(self, filename):
        """
        Param filename: LLVM compiled filename
        """
        with open(filename, "w") as f:
            f.write(repr(self.module))


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
    v.save(output_filename)