from swlab_parser.lib.CommonParserUtil import CommonParserUtil
from swlab_parser.parser.Token import Token
from swlab_parser.lib.TokenBuilder import TokenBuilder
import os

class Lexer:

    pu = CommonParserUtil()

    def __init__(self, pu):
        begin = lambda *args: args[-1]

        self.pu = pu
        #tb = TokenBuilder("", Token)

        self.pu.lex("[ \t\n]", lambda text: None)
        #self.pu.lex("[0-9]+", Token.INTEGER_NUMBER)
        self.pu.lex("[0-9]+", lambda text: Token.END_OF_TOKEN)

        self.pu.lex("(", lambda text: Token.OPEN_PAREN)
        self.pu.lex(")", lambda text: Token.CLOSE_PAREN)

        self.pu.lex("+", lambda text: Token.ADD)
        self.pu.lex("-", lambda text: Token.SUB)
        self.pu.lex("*", lambda text: Token.MUL)
        self.pu.lex("/", lambda text: Token.DIV)

        self.pu.lex("=", lambda text: Token.EQ)
        self.pu.lex(";", lambda text: Token.SEMICOLON)

        self.pu.lex("[a-zA-Z]+[a-zA-Z0-9]*", lambda text: Token.IDENTIFIER)
