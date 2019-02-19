#from parser.Token import Token
from swlab_parser.lib.TokenBuilder import TokenBuilder

class CommonParserUtil():

    workingdir = "./"

    def __init__(self):
        self.terminalList = []

        self.stack = []

        self.action_table = []
        self.goto_table = []
        self.grammar_rules = {}

        self.treeBuilders = {}
        self.tokenBuilders = {}

    def lex(self, regExp, tb):
        self.tokenBuilders[regExp] = tb
    def lexing(self, regExp):
        tb = self.tokenBuilders[regExp]
        token = tb("abc")
        print(token)


    def lexEndToken(self, regExp, tb):
        self.tokenBuilders[regExp] = tb
        self.endOfTok = regExp

    def ruleStartSymbol(self, startSymbol):
        self.startSymbol = startSymbol

    def rule(self, productionRule, tb):
        self.treeBuilders[productionRule.replace(" ", "")] = tb

    def get(self, i):
        productionRuliStr = self.grammar_rules[productionRuleIdx]