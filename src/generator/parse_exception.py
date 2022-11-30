
class BaseException(Exception):
    pass


class InitializationException(BaseException):
    def __init__(self, variable):
        self.variable = variable

    def __str__(self):
        return f"Variable \"" + self.variable + "\" must be initialized first."
