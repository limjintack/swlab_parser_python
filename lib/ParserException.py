import sys


class ParserException(Exception):

    def __init__(self, message):
        super()
        self.message = message
        print(message, file=sys.stderr)

    def __init__(self, message, culprit, err_line_index, err_ch_index):
        super()
        self.message = message
        print(message, " ", culprit, " ", err_line_index, ", ", err_ch_index, file=sys.stderr)
