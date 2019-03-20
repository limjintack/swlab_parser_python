import os

from swlab_parser_python.example.ast.Interp import Interp
from swlab_parser_python.example.ast.Expr import Expr
from swlab_parser_python.example.parser.Parser import Parser
from swlab_parser_python.example.parser.Lexer import Lexer
from swlab_parser_python.lib.CommonParserUtil import CommonParserUtil


class Main:

    def __init__(self):
        base = os.path.expanduser('~')
        prj = "PycharmProjects\\Project\\swlab_parser_python\\example"

        while True:
            filename = input("Enter your file name: ")
            file = open(base + "\\" + prj + "\\" + filename, mode='r', encoding='utf-8')

            parser = Parser()
            exprSeq = parser.Parsing(file)

            pretty_test = Expr()
            pretty_test.prettyPrint(exprSeq);

            env = {}
            Interp_test = Interp()
            Interp_test.seq(exprSeq, env)

            print("x = ", env["x"])
            print("abcd = ", env["abcd"])



Main()