
class BaseException(Exception):
    pass


class VariableInitializationException(BaseException):
    def __init__(self, variable):
        self.variable = variable

    def __str__(self):
        return f"Variable \"" + self.variable + "\" must be initialized first."

class VariableNotDefineException(BaseException):
    def __init__(self, variable):
        self.variable = variable

    def __str__(self):
        return f"Variable \"" + self.variable + "\" is not defined."

class FunctionNameDuplicateException(BaseException):
    def __init__(self, funcname):
        self.funcname = funcname

    def __str__(self):
        return f"Function name \"" + self.funcname + "\" duplicate."

class TypeMisatchException(BaseException):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self):
        return f"Type mismatch \"" + self.expr1 + "\", \"" + self.expr2 + "\""

class TypeUnknownException(BaseException):
    def __init__(self, variable):
        self.variable = variable

    def __str__(self):
        return f"Type unknown \"" + self.variable + "\""

