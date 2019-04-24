from example.ast.Expr import Expr


class Var(Expr):
    def __init__(self, varName):
        self.varName = varName

    def getVarNmae(self):
        return self.varName

    def toString(self):
        return self.varName