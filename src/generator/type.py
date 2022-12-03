from llvmlite import ir

void = ir.VoidType()
byte = ir.IntType(8)
boolean = ir.IntType(1)
int32 = ir.IntType(32)
float = ir.FloatType()
char = ir.IntType(8)
void_p = byte.as_pointer()
"""
string
function
userdata
thread
table
"""

class ClassType:
    def __init__(self, name: str, llvm_type: ir.BaseStructType):
        self._name = name
        self._llvm_type = llvm_type

        self._elems: list[ir.Type] = []
        self._elem_pos: dict[str, int] = {}

    @classmethod
    def construct(cls, name: str, fields: dict):
        struct_type = ClassType(name, ir.LiteralStructType([]))
        for name, typ in fields.items():
            struct_type.add_field(name, typ)
        return struct_type

    def add_field(self, name: str, type: ir.Type):
        self._elem_pos[name] = len(self._elems)
        self._elems.append(type)
        self._llvm_type.elements = tuple(self._elems)

    def index_of(self, name: str) -> int:
        return self._elem_pos[name]

    @property
    def name(self) -> str:
        return self._name

    @property
    def p_type(self) -> ir.PointerType:
        return self._llvm_type.as_pointer()

    @property
    def type(self) -> ir.BaseStructType:
        return self._llvm_type