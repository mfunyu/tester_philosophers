from pyparsing import *

class Parse():

    def delete_escapesquence(str):
        ESC = Literal('\x1b')
        integer = Word(nums)
        escapeSeq = Combine(ESC + '[' + Optional(delimitedList(integer,';')) +
                oneOf(list(alphas)))

        nonAnsiString = lambda s : Suppress(escapeSeq).transformString(s)

        unColorString = nonAnsiString(str)

        return unColorString
