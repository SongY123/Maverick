from llvmlite import ir

nil = ir.VoidType()
byte = ir.IntType(8)
boolean = ir.IntType(1)
int32 = ir.IntType(32)
float = ir.FloatType()
"""
string
function
userdata
thread
table
"""
