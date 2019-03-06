from swlab_parser_python.example.ast.Expr import Expr


class BinOp(Expr):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

    def __init__(self, opKind, left, right):
        self.opKind = opKind
        self.left = left
        self.right = right

    def getOpKind(self):
        return self.opKind
    def getLeft(self):
        return self.left
    def getRigth(self):
        return self.right

    def toString(self):
        opstr = ""
        if self.opKind == self.ADD:
            opstr = "+"
        elif self.opKind == self.SUB:
            opstr = "-"
        elif self.opKind == self.MUL:
            opstr = "*"
        elif self.opKind == self.DIV:
            opstr = "/"
        else:
            return False

        exprstr = self.left.toString() + " " + opstr + " " + self.right.toString()
        return "(" + exprstr + ")"
