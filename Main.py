import os
#from Main.parser.Parser import Parser
from swlab_parser.parser.Lexer import Lexer
from swlab_parser.lib.CommonParserUtil import CommonParserUtil


class Main:

    def __init__(self):
        base = os.path.expanduser('~')
        prj = "PycharmProjects/Project/Main/example"
        pu = CommonParserUtil()
        lexer = Lexer(pu)
        print(lexer.pu.tokenBuilders)
        pu.lexing("(")

'''
        while(1):
            name = input("Enter your file name: ")
            file = open(base + "/" + prj + "/" + name, mode='rt', encoding='utf-8')
'''
Main()