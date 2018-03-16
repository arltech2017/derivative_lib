#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = "__init__"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


def normalize(self):
    if isinstance(self, Symbol):
        return self
    elif isinstance(self, Addition):
        return self
    return Symbol(self)

class Symbol():
    def __init__(self, data):
        self.data = data

    def __eq__(self, op):
        return normalize(self) == normalize(op)

    def __add__(self, op):
        return Addition(self, op)


class Addition():
    def __init__(self, op1, op2):
        self.op1 = normalize(op1)
        self.op2 = normalize(op2)

    def __str__(self):
        return str(self.op1) + " + " + str(self.op2)

    def __add__(self, op):
        return Addition(self, op)
