#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = "__main__"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


from __init__ import *
print(dir())
symbols = {'*': Multiplication, '**': Power, '+': Addition}


def tryToDigit(numeric_string):
    try:
        return float(numeric_string)
    except ValueError:
        return False


def translate(symbol):
    if symbol in symbols:
        return symbols[symbol]
    elif tryToDigit(symbol) is not None:
        return Number(tryToDigit(symbol))
    else:
        return Symbol(symbol)


while True:
    z = input().split()
    print([translate(i) for i in z])
