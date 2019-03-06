import re
import os

from swlab_parser_python.lib.Nonterminal import Nonterminal
from swlab_parser_python.lib.ParseState import ParseState
from swlab_parser_python.lib.Terminal import Terminal


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

        self.productionRuleIdx = 0

    def lex(self, regExp, TokFunc):
        self.tokenBuilders[regExp] = TokFunc

    def lexing(self, reader):
        ps = []
        lineArr = reader.readlines()
        keys = list(self.tokenBuilders.keys())
        lineno = 1

        for index in range(len(keys)):
            ps.append(re.compile(keys[index]))

        for line_idx in range(len(lineArr)):
            line = lineArr[line_idx].rstrip("\n")

            front_idx = 0
            endIdx = 0
            while front_idx < len(line):
                for i in range(len(keys)):
                    regExp = keys[i]
                    p = ps[i]
                    matcher = p.match(line, front_idx)

                    if matcher != None:
                        startIdx = matcher.start()
                        endIdx = matcher.end()

                        str = line[startIdx:endIdx]
                        tb = self.tokenBuilders[regExp]

                        front_idx = endIdx

                        if tb(str):
                            self.terminalList.append(Terminal(str, tb(str), startIdx, lineno))
                        break

            lineno += 1
        tb = self.tokenBuilders[self.endOfTok]
        self.terminalList.append(Terminal(self.endOfTok, tb(self.endOfTok), -1, -1))

    def lexEndToken(self, regExp, tb):
        self.tokenBuilders[regExp] = tb
        self.endOfTok = regExp

    def ruleStartSymbol(self, startSymbol):
        self.startSymbol = startSymbol

    def rule(self, productionRule, tb):
        self.treeBuilders[productionRule.rstrip()] = tb

    def get(self, i):
        productionRuleStr = self.grammar_rules[self.productionRuleIdx]
        splitRule = productionRuleStr.split()
        length = len(splitRule) - 2

        last_stack_tree_index = len(self.stack) - 1
        offset = (length * 2) - ((i - 1) * 2 + 1)
        nt = self.stack[last_stack_tree_index - offset]

        return nt.getTree()

    def getText(self, i):
        productionRuleStr = self.grammar_rules[self.productionRuleIdx]
        splitRule = productionRuleStr.split()
        length = len(splitRule) - 2

        last_stack_tree_index = len(self.stack) - 1
        offset = (length * 2) - ((i - 1) * 2 + 1)
        nt = self.stack[last_stack_tree_index - offset]

        return nt.getSyntax()

    def readInitialize(self):
        self.grammar_rules.clear();
        self.action_table.clear();
        self.goto_table.clear();

        grammarFReader = open(os.getcwd() + "\\grammar_rules.txt", mode='r', encoding='utf-8')
        actionFReader = open(os.getcwd() + "\\action_table.txt", mode='r', encoding='utf-8')
        gotoFReader = open(os.getcwd() + "\\goto_table.txt", mode='r', encoding='utf-8')

        for line in grammarFReader:
            arr = line.rstrip().split(":", 2)
            grammerNum = int(arr[0].replace(" ", ""))
            grammer = arr[1].strip()

            self.grammar_rules[grammerNum] = grammer

        for line in actionFReader:
            self.action_table.append(line.rstrip())

        for line in gotoFReader:
            self.goto_table.append(line.rstrip())

        grammarFReader.close();
        actionFReader.close();
        gotoFReader.close();

    def parsing(self, reader):
        self.readInitialize()

        self.lexing(reader)

        self.stack.clear()
        self.stack.append(ParseState("0"))

        while self.terminalList:
            currentState = self.stack[-1]
            currentTerminal = self.terminalList[0]

            data_arr = self.Check_state(currentState, currentTerminal, self.terminalList)
            order = data_arr[0]
            print(data_arr)

            if order == "Accept":
                self.terminalList.pop(0)
                return self.stack[1].getTree()
            elif order == "Shift":
                state = data_arr[1]
                self.stack.append(currentTerminal)
                self.stack.append(ParseState(state))
                self.terminalList.pop(0)
            elif order == "Reduce":
                grammar_rule_num = int(data_arr[1])
                self.productionRuleIdx = grammar_rule_num

                grammar_rule = self.grammar_rules[grammar_rule_num]
                reduce_arr = grammar_rule.split('->')
                lhs = reduce_arr[0].split()

                if len(reduce_arr) > 1 and len(reduce_arr[1]) > 0:
                    rhs = reduce_arr[1]
                    rhsLength = len(rhs.split())
                else:
                    rhs = ""
                    rhsLength = 0

                tr_b = self.treeBuilders[grammar_rule]()
                if tr_b is not None:
                    tree = tr_b
                else:
                    print("error")

                for leng in range(rhsLength):
                    self.stack.pop()
                    self.stack.pop()

                currentState = self.stack[-1]
                self.stack.append(Nonterminal(tree))
                self.stack.append(self.get_st(currentState, lhs, self.terminalList))

    def Check_state(self, current_state, terminal, token):
        for actionTable_str in self.action_table:
            data = actionTable_str.split()

            return_data = []

            if current_state.getState() == data[0]:
                index = 1

                ''' # 자바와 파이썬 split 차이인지 쓰이질 않음.
                while data[index] == "" or data[index] == "\t":
                    index = index + 1
                '''

                index_Token = terminal.getToken().toToken(data[index])
                if terminal.getToken() == index_Token:
                    for i in range(index + 1, len(data)):
                        if data[i] == "":
                            continue
                        return_data.append(data[i])
                    return return_data

    def get_st(self, current_state, index, tokens):
        count = 0
        location = 0

        while count < len(self.goto_table):
            st_tr_arr = self.goto_table[count].split()
            while location < len(st_tr_arr):
                start_state = st_tr_arr[location]
                if current_state.getState() == start_state:
                    location += 1
                    if st_tr_arr[location] == index[0]:
                        location += 1
                        if st_tr_arr[location] != "":
                            return ParseState(st_tr_arr[location])
                        else:
                            break
                    else:
                        break
                else:
                    break
            count += 1
            location = 0