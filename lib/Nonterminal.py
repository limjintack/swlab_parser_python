from swlab_parser_python.lib.StkElem import StkElem


class Nonterminal(StkElem):
    def __init__(self, tree):
        super()
        self.tree = tree

    def getTree(self):
        return self.tree

    def setTree(self, tree):
        self.tree = tree

    def toString(self):
        if self.tree == None:
            return "null"
        else:
            return self.tree