from lib.StkElem import StkElem


class Terminal(StkElem):
    def __init__(self, syntax, token, chIndex, lineIndex):
        super()
        self.syntax = syntax
        self.token = token
        self.chIndex = chIndex
        self.lineIndex = lineIndex

    def getToken(self):
        return self.token

    def getSyntax(self):
        return self.syntax

    def getchIndex(self):
        return self.chIndex

    def getlineIndex(self):
        return self.lineIndex