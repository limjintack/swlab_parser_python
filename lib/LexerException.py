

class LexerException(Exception):

    def __init__(self, message):
        super()
        self.message = message

    def getMessage(self):
        return self.message

    def setMessage(self, message):
        self.message = message