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
    def test__repr__(self, a):
        self.assertEqual(str(a), str(Symbol(a)))

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

    valid_numbers = [(st.integers() | st.floats(allow_nan=False))]

    @given(*valid_symbols)
    def test__init__(self, a, b):
        Addition(a, b)

    @given(*valid_symbols)
    def test__repr__(self, a, b):
        self.assertEqual(str(a) + ' + ' + str(b), repr(Addition(a, b)))

    @given(*(valid_numbers * 2))
    def test__eq__(self, a, b):
        self.assertEqual(a + b, Addition(a, b))

    @given(*(valid_numbers) * 2)
    def test_implicit_init(self, a, b):
        self.assertIsInstance(Symbol(a) + Symbol(b), Addition)
        self.assertEqual(Addition(a, b), Symbol(a) + Symbol(b))

    @given(*(valid_numbers * 5))
    def test__add__(self, a, b, c, d, e):
        addition_expression1 = Addition(a, b)
        addition_expression2 = Addition(c, d)
        symbol1 = Symbol(e)

        self.assertIsInstance(addition_expression1 + addition_expression2,
                              Addition)

        self.assertIsEqual(a + b + c + d,
                           addition_expression1 + addition_expression2)

        self.assertIsInstance(addition_expression1 + symbol1,
                              Addition)
        self.assertIsEqual(a + b + e,
                           addition_expression1 + symbol1)


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
