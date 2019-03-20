from swlab_parser_python.example.ast.Assign import Assign
from swlab_parser_python.example.ast.BinOp import BinOp
from swlab_parser_python.example.ast.Lit import Lit
from swlab_parser_python.example.ast.Var import Var
from swlab_parser_python.lib.CommonParserUtil import CommonParserUtil
from swlab_parser_python.example.parser.Lexer import Lexer

class Parser:
    def __init__(self):
        self.pu = CommonParserUtil()
        begin = lambda *args: args[-1]

        seqexpr = []

        Lexer(self.pu);

        self.pu.ruleStartSymbol("SeqExpr'")

        self.pu.rule("SeqExpr' -> SeqExpr",
                     lambda : begin(self.pu.get(1)))
        self.pu.rule("SeqExpr -> SeqExpr ; AssignExpr",
                     lambda: begin(seqexpr.append(self.pu.get(3)), seqexpr))

        self.pu.rule("SeqExpr -> AssignExpr",
                     lambda: begin(seqexpr.append(self.pu.get(1)), seqexpr))
        self.pu.rule("AssignExpr -> identifier = AssignExpr",
                     lambda: begin(Assign(self.pu.getText(1), self.pu.get(3))))
        self.pu.rule("AssignExpr -> AdditiveExpr",
                     lambda: begin(self.pu.get(1)))
        self.pu.rule("AdditiveExpr -> AdditiveExpr + MultiplicativeExpr",
                     lambda: begin(BinOp(BinOp.ADD, self.pu.get(1), self.pu.get(3))))
        self.pu.rule("AdditiveExpr -> AdditiveExpr - MultiplicativeExpr",
                     lambda: begin(BinOp(BinOp.SUB, self.pu.get(1), self.pu.get(3))))
        self.pu.rule("AdditiveExpr -> MultiplicativeExpr",
                     lambda: begin(self.pu.get(1)))
        self.pu.rule("MultiplicativeExpr -> MultiplicativeExpr * PrimaryExpr",
                     lambda: begin(BinOp(BinOp.MUL, self.pu.get(1), self.pu.get(3))))
        self.pu.rule("MultiplicativeExpr -> MultiplicativeExpr / PrimaryExpr",
                     lambda: begin(BinOp(BinOp.DIV, self.pu.get(1), self.pu.get(3))))
        self.pu.rule("MultiplicativeExpr -> PrimaryExpr",
                     lambda: begin(self.pu.get(1)))
        self.pu.rule("PrimaryExpr -> identifier",
                     lambda: begin(Var(self.pu.getText(1))))
        self.pu.rule("PrimaryExpr -> integer_number",
                     lambda: begin(Lit(int(self.pu.getText(1)))))
        self.pu.rule("PrimaryExpr -> ( AssignExpr )",
                     lambda: begin(self.pu.get(2)))

    def Parsing(self, reader):
        return self.pu.parsing(reader)