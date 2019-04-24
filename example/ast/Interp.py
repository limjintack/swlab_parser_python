from example.ast.Assign import Assign
from example.ast.Lit import Lit
from example.ast.Var import Var
from example.ast.BinOp import BinOp

class Interp:

    def __init__(self):
        None

    def seq(self, exprList, env):
        index = 0

        while index < len(exprList):
            self.expr(exprList[index], env)
            index += 1

    def expr(self, expr, env):
        if isinstance(expr, BinOp):
            binOpExpr = expr

            leftV = self.expr(binOpExpr.getLeft(), env)
            rightV = self.expr(binOpExpr.getRigth(), env)

            if binOpExpr.getOpKind() == BinOp.ADD:
                return leftV + rightV
            elif binOpExpr.getOpKind() == BinOp.SUB:
                return leftV - rightV
            elif binOpExpr.getOpKind() == BinOp.MUL:
                return leftV * rightV
            elif binOpExpr.getOpKind() == BinOp.DIV:
                return leftV / rightV
            else:
                return False

        elif isinstance(expr, Assign):
            assignExpr = expr
            varName = assignExpr.getvarNmae()
            rhs = assignExpr.getRhs()

            rhsV = self.expr(rhs, env)
            env[varName] = rhsV

        elif isinstance(expr, Lit):
            litExpr = expr
            iniLitV = litExpr.getInteger()

            return iniLitV

        elif isinstance(expr, Var):
            varExpr = expr
            varName = varExpr.getVarNmae()
            varV = env[varName]

            return varV

        else:
            return False

        return 0