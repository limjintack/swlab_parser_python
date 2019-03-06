

class Expr:
    def __init__(self):
        None

    def prettyPrint(self, exprSeq):
        index = 0
        print("-------------------PrettyPrint---------------------")
        while(index < len(exprSeq)):
            if index + 1 < len(exprSeq):
                delimeter = ";"
            else:
                delimeter = ""
            print(exprSeq[index].toString(), delimeter)
            index = index + 1
        print("---------------------------------------------------")