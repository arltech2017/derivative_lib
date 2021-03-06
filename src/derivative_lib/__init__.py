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
import numbers

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
        return Addition(self, op).simplify()

    def __sub__(self, op):
        return Subtraction(self, op).simplify()

    def __mul__(self, op):
        return Multiplication(self, op).simplify()

    def __truediv__(self, op):
        return Division(self, op).simplify()

    def __pow__(self, op):
        return Power(self, op).simplify()

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

    def derivative(self):
        return Number(1)

    def simplify(self):
        return self


class Number(Symbol):
    @property
    def negative(self):
        return self.data[0] < 0

    def __init__(self, data):
        self.data = (data,)

    def __eq__(self, op):
        return self.data == normalize(op).data

    def __hash__(self):
        return hash(self.data)

    def __str__(self):
        return str(self.data[0])

    def __add__(self, op):
        if isinstance(op, Number):
            return Number(self.data[0] + op.data[0])
        return super().__add__(op)

    def __sub__(self, op):
        if isinstance(op, Number):
            return Number(self.data[0] - op.data[0])
        return super().__sub__(op)

    def __mul__(self, op):
        if isinstance(op, Number):
            return Number(self.data[0] * op.data[0])
        return super().__mul__(op)

    def __truediv__(self, op):
        if isinstance(op, Number):
            if op.data[0] == 0:
                return "INFINITY"
            return Number(self.data[0] / op.data[0])
        return super().__truediv__(op)

    def __pow__(self, op):
        if isinstance(op, Number):
            return Number(self.data[0] ** op.data[0])
        return super().__pow__(op)

    def __neg__(self):
        return Number(-self.data[0])

    def derivative(self):
        return Number(0)


class Addition(Symbol):
    @property
    def negative(self):
        return False

    def __init__(self, op1, op2):
        self.data = (normalize(op1), normalize(op2))

    def __str__(self):
        return "(" + str(self.data[0]) + " + " + str(self.data[1]) + ")"

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, op):
        return Counter(self.data) == Counter(op.data) and isinstance(op, Addition)

    def __neg__(self):
        return Subtraction(-self.data[0], self.data[1])

    def simplify(self):
        if self.data[0] == Number(0):
            return self.data[1]
        elif self.data[1] == Number(0):
            return self.data[0]
        elif self.data[0] == self.data[1]:
            return self.data[0] * Number(2)

        if self.data[1].negative:
            return self.data[0] - (-self.data[1])
        elif self.data[0].negative:
            return self.data[1] - (-self.data[0])

        return self

    def derivative(self):
        return self.data[0].derivative() + self.data[1].derivative()

class Subtraction(Addition):
    @property
    def negative(self):
        return False

    def __init__(self, op1, op2):
        self.data = (normalize(op1), -normalize(op2))

    def __str__(self):
        return "(" + str(self.data[0]) + " - " + str(-self.data[1]) + ")"

    def simplify(self):
        if self.data[0] == Number(0):
            return -self.data[1]
        elif self.data[1] == Number(0):
            return self.data[0]
        elif self.data[0] == self.data[1]:
            return Number(0)
        return self

    def derivative(self):
        return self.data[0].derivative() - self.data[1].derivative()

class Multiplication(Symbol):
    @property
    def negative(self):
        return False

    def __init__(self, op1, op2):
        self.data = (normalize(op1), normalize(op2))

    def __str__(self):
        return "(" + str(self.data[0]) + " * " + str(self.data[1]) + ")"

    def __eq__(self, op):
        return Counter(self.data) == Counter(op.data) and isinstance(op, Multiplication)

    def __hash__(self):
        return hash(self.data)

    def __neg__(self):
        return -self.data[0] ** self.data[1]

    def simplify(self):
        if self.data[0] == Number(0) or self.data[1] == Number(0):
            return Number(0)
        if self.data[0] == Number(1):
            return self.data[1]
        elif self.data[0] == Number(-1) and not isinstance(self.data[1], Power): #How do you make a power function negative?
            return -self.data[1]
        elif self.data[1] == Number(1):
            return self.data[0]
        elif self.data[1] == Number(-1):
            return -self.data[0]
        elif self.data[0] == self.data[1]:
            return self.data[0] ** Number(2)
        return self

    def derivative(self):
        return (self.data[0].derivative() * self.data[1]) + (self.data[0] * self.data[1].derivative())

#def Division(op1, op2):
    #return normalize(op1) * (normalize(op2) ** -1)

class Division(Multiplication):
    def __init__(self, op1, op2):
        self.data = (normalize(op1), normalize(op2) ** -1)

    def __str__(self):
        return "(" + str(self.data[0]) + " / " + str(self.data[1] ** -1) + ")"


class Power(Symbol):
    @property
    def negative(self):
        return False

    def __init__(self, op1, op2):
        self.data = (normalize(op1), normalize(op2))

    def __str__(self):
        return "(" + str(self.data[0]) + " ** " + str(self.data[1]) + ")"

    def __eq__(self, op):
        return self.data == op.data

    def __hash__(self):
        return hash(str(self))

    def __neg__(self):
        return Number(-1)

    def simplify(self):
        if isinstance(self.data[0], Power):
            return (self.data[0].data[0] ** (self.data[0].data[1] * self.data[1]))
        if self.data[1] == Number(0):
            return Number(1)
        if self.data[1] == Number(1):
            return self.data[0]
        if self.data[0] == Number(0): #must come after self.data[1] == 0
            return Number(0)
        return self

    def derivative(self):
        x = self.data[0] ** (self.data[1] - Number(1))
        y = self.data[0].derivative()
        z = x * y
        print(z)
        print(self.data[1])
        print(self.data[1] * z)
        return (self.data[1] * ((self.data[0] ** (self.data[1] - Number(1))) * self.data[0].derivative()))
