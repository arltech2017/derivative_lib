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


class Symbol():
    def __init__(self, data):
        self.data = data

    def __eq__(self, op):
        if isinstance(op, Symbol):
            return self.data == op.data
        return self.data == op

    def __add__(self, op):
        if isinstance(op, Symbol):
            try:
                return self.data + op.data
            except TypeError:
                pass
        elif isinstance(op, Expression):
            pass
        else:
            return self + Symbol(op)

    def __sub__(self, op):
        if isinstance(op, Symbol):
            try:
                return self.data - op.data
            except TypeError:
                pass
        elif isinstance(op, Expression):
            pass
        else:
            return self - Symbol(op)

    def __mul__(self, op):
        if isinstance(op, Symbol):
            try:
                return self.data * op.data
            except TypeError:
                pass
        elif isinstance(op, Expression):
            pass
        else:
            return self * Symbol(op)

    def __truediv__(self, op):
        if isinstance(op, Symbol):
            try:
                return self.data / op.data
            except TypeError:
                pass
        elif isinstance(op, Expression):
            pass
        else:
            return self / Symbol(op)

    def __str__(self):
        return str(self.data)

class Addition():
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def __repr__(self):
        return str(self.op1) + " + " + str(self.op2)

class Expression():
    pass
