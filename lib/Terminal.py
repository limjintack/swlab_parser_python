from swlab_parser_python.lib.StkElem import StkElem


class Terminal(StkElem):
    def __init__(self, syntax, token, chIndex, lineIndex):
        super()
        self.syntax = syntax
        self.token = token
        self.chIndex = chIndex
        self.lineIndex = lineIndex

    def getToken(self):
        return self.token