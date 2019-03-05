import os
from swlab_parser_python.example.parser.Parser import Parser
from swlab_parser_python.example.parser.Lexer import Lexer
from swlab_parser_python.lib.CommonParserUtil import CommonParserUtil


class Main:

    def __init__(self):
        base = os.path.expanduser('~')
        prj = "PycharmProjects\\Project\\swlab_parser_python\\example"

        while True:
            filename = input("Enter your file name: ")
            filename = "test.txt"
            file = open(base + "\\" + prj + "\\" + filename, mode='r', encoding='utf-8')

            parser = Parser()
            parser.Parsing(file)


Main()