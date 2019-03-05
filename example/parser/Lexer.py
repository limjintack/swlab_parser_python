from swlab_parser_python.lib.CommonParserUtil import CommonParserUtil
from swlab_parser_python.example.parser.Token import Token

class Lexer:

    pu = CommonParserUtil()

    def __init__(self, pu):
        self.pu = pu

        self.pu.lexEndToken("\$", lambda text: Token.END_OF_TOKEN)

        self.pu.lex("[\s]", lambda text: None)
        self.pu.lex("[0-9]+", lambda text: Token.INTEGER_NUMBER)

        self.pu.lex("\(", lambda text: Token.OPEN_PAREN)
        self.pu.lex("\)", lambda text: Token.CLOSE_PAREN)

        self.pu.lex("\+", lambda text: Token.ADD)
        self.pu.lex("\-", lambda text: Token.SUB)
        self.pu.lex("\*", lambda text: Token.MUL)
        self.pu.lex("\/", lambda text: Token.DIV)

        self.pu.lex("\=", lambda text: Token.EQ)
        self.pu.lex("\;", lambda text: Token.SEMICOLON)

        self.pu.lex("[a-zA-Z]+[a-zA-Z0-9]*", lambda text: Token.IDENTIFIER)
