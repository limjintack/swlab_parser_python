import os
import traceback

from example.ast.Interp import Interp
from example.ast.Expr import Expr
from example.parser.Parser import Parser
from example.parser.Lexer import Lexer
from lib.CommonParserUtil import CommonParserUtil
from lib.ParserException import ParserException
from lib.LexerException import LexerException


class Main:

    def __init__(self):
        base = os.path.expanduser('~')
        prj = "PycharmProjects\\Project\\swlab_parser_python\\example"

        while True:
            try:
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

            except FileNotFoundError as e:
                print("Not found: ", base, "\\", prj, "\\", filename, sep="")
            except Lexer:
                traceback.print_exc()
            except ParserException:
                traceback.print_exc()
            except Exception:
                traceback.print_exc()


Main()
