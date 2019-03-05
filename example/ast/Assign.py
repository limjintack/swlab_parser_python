from swlab_parser_python.example.ast.Expr import Expr


class Assign(Expr):
    def __init__(self, varName, rhs):
        self.varName = varName
        self.rhs = rhs

    def getvarNmae(self):
        return self.varName

    def getRhs(self):
        return self.rhs

    def toString(self):
        exprStr = self.varName + " = " + self.rhs
        return "(" + exprStr + ")"