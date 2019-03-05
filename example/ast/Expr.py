

class Expr:
    def __init__(self):
        None

    def prettyPrint(self, exprSeq):
        index = 0
        while(index < len(exprSeq)):
            if index + 1 < len(exprSeq):
                delimeter = ";"
            else:
                delimeter = ""
            print(exprSeq[index] + delimeter)
            index = index + 1