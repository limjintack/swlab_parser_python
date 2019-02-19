from enum import Enum


class Token(Enum):
    END_OF_TOKEN = "$"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    IDENTIFIER = "identifier"
    INTEGER_NUMBER = "integer_number"
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    EQ = "="
    SEMICOLON = ";"

    def __init__(self, strToken):
        self.strToken = strToken

    def toToken(self, str):
        for token in self.value:
            if (self.strToken == str):
                return self
            else:
                return print("error")

    def toString(self, tok):
        return tok.strToken
