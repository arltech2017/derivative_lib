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

from collections import Counter
import numbers.Number

def normalize(self):
    if isinstance(self, Symbol):
        return self
    if isinstance(self, numbers.Number):
        return Number(self)
    return Symbol(self)


class Symbol():
    def __init__(self, data):
        self.data = (data,)
        self.negative = False

    def __eq__(self, op):
        return str(self.data) == str(normalize(op).data)

    def __add__(self, op):
        return Addition(self, op)

    def __sub__(self, op):
        return Subtraction(self, op)

    def __mul__(self, op):
        return Multiplication(self, op)

    def __truediv__(self, op):
        return Division(self, op)

    def __pow__(self, op):
        return Power(self, op)

    def __str__(self):
        s = ""
        if self.negative:
            s+='-'
        return s + str(self.data[0])

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def __neg__(self):
        s = Symbol(self.data[0])
        s.negative = self.negative ^ True
        return s 


class Number(Symbol):
    def __init__(self, data):
        self.data = (data,)

    def __add__(self, op):
        if isinstance(op, Number):
            return self.data[0] + op.data[0]
        return super().__add__(op)

    def __sub__(self, op):
        if isinstance(op, Number):
            return self.data[0] - op.data[0]
        return super().__sub__(op)

    def __mul__(self, op):
        if isinstance(op, Number):
            return self.data[0] * op.data[0]
        return super().__mul__(op)

    def __truediv__(self, op):
        if isinstance(op, Number):
            return self.data[0] / op.data[0]
        return super().__truediv__(op)

    def __pow__(self, op):
        if isinstance(op, Number):
            return self.data[0] ** op.data[0]
        return super().__pow__(op)

    def __neg__(self):
        return Number(-self.data[0])


class Addition(Symbol):
    def __init__(self, op1, op2):
        self.data = (normalize(op1), normalize(op2))

    def __str__(self):
        return str(self.data[0]) + " + " + str(self.data[1])

    def __eq__(self, op):
        return Counter(self.data) == Counter(op.data) and isinstance(op, Addition)

    def __neg__(self):
        return Subtraction(-self.data[0], self.data[1])

class Subtraction(Addition):
    def __init__(self, op1, op2):
        self.data = (normalize(op1), -normalize(op2))

    def __str__(self):
        return str(self.data[0]) + " - " + str(-self.data[1])

class Multiplication(Symbol):
    def __init__(self, op1, op2):
        self.data = (normalize(op1), normalize(op2))

    def __str__(self):
        return str(self.data[0]) + " * " + str(self.data[1])

    def __eq__(self, op):
        return Counter(self.data) == Counter(op.data) and isinstance(op, Multiplication)

    def __neg__(self):
        return Multiplication(-self.data[0], self.data[1])

class Division(Multiplication):
    def __init__(self, op1, op2):
        self.data = (normalize(op1), normalize(op2) ** -1)

    def __str__(self):
        return str(self.data[0]) + " / " + str(self.data[1])

class Power(Symbol):
    def __init__(self, op1, op2):
        self.data = (normalize(op1), normalize(op2))

    def __str__(self):
        return str(self.data[1]) + " ** " + str(self.data[2])

    def __eq__(self, op):
        return self.data == op.data
