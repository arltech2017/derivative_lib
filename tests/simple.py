#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import unittest
from hypothesis import given
from hypothesis import strategies as st
import string

from derivative_lib import Equation, Symbol

__appname__     = "simple"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


class Init(unittest.TestCase):
    @given(st.integers() |
           st.floats() |
           st.text(string.ascii_letters, min_size=1))
    def testSymbolGeneric(self, a):
        Symbol(a)


class Equality(unittest.TestCase):
    @given(st.integers())
    def testEqualityInt(self, a):
        self.assertEquals(Symbol(a), Symbol(a))

    @given(st.integers() |
           st.floats() |
           st.text(string.ascii_letters, min_size=1))
    def testEqualityGeneric(self, a):
        self.assertEquals(Symbol(a), Symbol(a))


class Addition(unittest.TestCase):
    @given(st.integers(), st.integers())
    def testPrintsTrue(self, a, b):
        import operator
        addition = Equation(2, operator.add, "{args[0]} - {args[1]}")
        self.assertEquals(Symbol(a + b), addition(Symbol(a), Symbol(b)))
