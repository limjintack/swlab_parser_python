from swlab_parser_python.example.ast.Expr import Expr

class Lit(Expr):
    def __init__(self, i):
        self.integerLit = i

    def getInteger(self):
        return self.integerLit

    def toString(self):
        return str(self.integerLit)