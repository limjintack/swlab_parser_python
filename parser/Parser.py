from swlab_parser.lib.CommonParserUtil import CommonParserUtil
from swlab_parser.parser.Lexer import Lexer

class Parser:
    def __init__(self):
        pu = CommonParserUtil()
        begin = lambda *args: args[-1]

        Lexer(pu);

        pu.ruleStartSymbol("SeqExpr'")
        #pu.rule("SeqExpr' -> SeqExpr", pu.get(1))

        pu.rule("SeqExpr' -> SeqExpr", lambda : pu.get(1))
        pu.rule("SeqExpr -> SeqExpr ; AssignExpr", lambda : begin()
        ArrayList < Expr > seqexpr = (ArrayList < Expr >)
        pu.get(1);
        Expr
        assignexpr = (Expr)
        pu.get(3);
        seqexpr.add(assignexpr);
        return seqexpr;});
