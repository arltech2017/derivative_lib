#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import unittest
from hypothesis import given, reproduce_failure
from hypothesis import strategies as st
import string

from derivative_lib import Symbol, Addition

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


class _Symbol(unittest.TestCase):
    valid_symbols = (st.integers() |
                     st.floats() |
                     st.text(string.ascii_letters, min_size=1))

    @given(valid_symbols)
    def test__init__(self, a):
        Symbol(a)

    @given(valid_symbols)
    def test__eq__(self, a):
        if a != a:  # For those pesky NaNs
            self.assertNotEqual(Symbol(a), Symbol(a))
        else:
            self.assertEqual(Symbol(a), Symbol(a))

    @given(valid_symbols, valid_symbols)
    def test__neq__(self, a, b):
        if a == b:
            return
        self.assertNotEqual(Symbol(a), Symbol(b))

    @given(st.integers(), st.integers())
    def test__add__(self, a, b):
        self.assertEqual(a + b, Symbol(a) + Symbol(b))

    @given(st.integers(), st.integers())
    def test__sub__(self, a, b):
        self.assertEqual(a - b, Symbol(a) - Symbol(b))

    @given(st.integers(), st.integers())
    def test__mul__(self, a, b):
        self.assertEqual(a * b, Symbol(a) * Symbol(b))

    @given(st.integers(), st.integers())
    def test__truediv__(self, a, b):
        if b == 0:
            return
        self.assertEqual(a / b, Symbol(a) / Symbol(b))


class _Addition(unittest.TestCase):
    valid_symbols = [(st.integers() |
                     st.floats() |
                     st.text(string.ascii_letters, min_size=1)) for _ in
                     range(2)]

    @given(*valid_symbols)
    def test__init__(self, a, b):
        Addition(a, b)

    def test__eq__(self, a, b):
        self.assertEqual(a + b, Addition(a, b))

    def test__repr__(self, a, b):
        self.assertEqual(repr(a) + ' + ' + repr(b), repr(Addition(a, b)))


"""
class _Expression(unittest.TestCase):
    def test_factory(self):
        import operator
        addition = Expression(operator.add)

    @given(st.integers(), st.integers())
    def test__eq__(self, a, b):
        import operator
        addition = Expression(operator.add)

        self.assertEqual(a + b, addition(a, b))
        self.assertEqual(a + b, addition(Symbol(a), Symbol(b)))
        """
