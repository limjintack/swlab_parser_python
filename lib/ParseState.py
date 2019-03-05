from swlab_parser_python.lib.StkElem import StkElem


class ParseState(StkElem):
    def __init__(self, state):
        super()
        self.state = state

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state