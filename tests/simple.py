#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import unittest
from hypothesis import given, reproduce_failure
from hypothesis import strategies as st
import string

from derivative_lib import Symbol, Number, Addition, Subtraction, Multiplication, Division, Power, normalize

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
    valid_symbol = st.text(string.ascii_letters, min_size=1)

    @given(valid_symbol)
    def test__init__(self, a):
        Symbol(a)

    @given(valid_symbol)
    def test__str__(self, a):
        self.assertEqual(str(a), str(Symbol(a)))

    @given(valid_symbol)
    def test__eq__(self, a):
        self.assertEqual(Symbol(a), Symbol(a))

    @given(valid_symbol, valid_symbol)
    def test__neq__(self, a, b):
        if a == b:
            return
        self.assertNotEqual(Symbol(a), Symbol(b))

    @given(*[valid_symbol] * 2)
    def test__add__(self, a, b):
        if a == b:
            self.assertIsInstance(Symbol(a) + Symbol(b), Multiplication)
        else:
            self.assertIsInstance(Symbol(a) + Symbol(b), Addition)

    @given(valid_symbol)
    def test_derivative(self, a):
        self.assertEqual(Symbol(a).derivative(), 1)

class _Number(unittest.TestCase):
    valid_numbers = st.integers()

    @given(valid_numbers)
    def test__str__(self, a):
        self.assertEqual(str(a), str(Number(a)))

    @given(*[valid_numbers] * 2)
    def test__eq__(self, a, b):
        if a == b:
            self.assertEqual(Number(a), Number(b))
        else:
            self.assertNotEqual(Number(a), Number(b))

    @given(*[valid_numbers] * 2)
    def test__add__(self, a, b):
        self.assertEqual(a + b, Number(a) + Number(b))

    @given(*[valid_numbers] * 2)
    def test__sub__(self, a, b):
        self.assertEqual(a - b, Number(a) - Number(b))

    @given(*[valid_numbers] * 2)
    def test__mul__(self, a, b):
        self.assertEqual(a * b, Number(a) * Number(b))

    @given(*[valid_numbers] * 2)
    def test__truediv__(self, a, b):
        if b == 0:
            return
        self.assertEqual(a / b, Number(a) / Number(b))

    @given(valid_numbers)
    def test__derivative__(self, a):
        self.assertEqual(Number(a).derivative(), 0)

class _Addition(unittest.TestCase):

    valid_symbols = st.text(string.ascii_letters, min_size=1)
    valid_numbers = st.integers()
    valid_num_sym = valid_symbols | valid_numbers

    @given(*[valid_num_sym] * 2)
    def test__init__(self, a, b):
        Addition(a, b)

    @given(*[valid_num_sym] * 2)
    def test__str__(self, a, b):
        self.assertEqual('(' + str(a) + ' + ' + str(b) + ')', str(Addition(a, b)))

    @given(*[valid_num_sym] * 2)
    def test__eq__(self, a, b):
        self.assertEqual(Addition(a, b), Addition(a, b))

        self.assertEqual(Addition(a, b), Addition(b, a))  # Commutative property

    @given(*[valid_num_sym] * 3)
    def test__neq__(self, a, b, c):
        self.assertNotEqual(Addition(a, b), Symbol(c))

    @given(*[valid_num_sym] * 4)
    def test__add__(self, a, b, c, d):
        if len(set([a, b, c, d])) != 4:
            return
        self.assertIsInstance(Addition(a, b) + Addition(c, d), Addition)

        self.assertIsInstance(Addition(a, b) + Symbol(c), Addition)
        self.assertIsInstance(Symbol(a) + Addition(b, c), Addition)

    @given(*[valid_num_sym] * 2)
    def test__derivative__(self, a, b):
        self.assertEqual(normalize(a).derivative() + normalize(b).derivative(), Addition(a, b).derivative())

class _Subtraction(unittest.TestCase):

    valid_symbols = st.text(string.ascii_letters, min_size=1)
    valid_numbers = st.integers()
    valid_num_sym = valid_symbols | valid_numbers

    @given(*[valid_num_sym] * 2)
    def test__init__(self, a, b):
        Subtraction(a, b)

    @given(*[valid_num_sym] * 2)
    def test__str__(self, a, b):
        self.assertEqual('(' + str(a) + ' - ' + str(b) + ')', str(Subtraction(a, b)))

    @given(*[valid_num_sym] * 2)
    def test__eq__(self, a, b):
        self.assertEqual(Subtraction(a, b), Subtraction(a, b))
        self.assertEqual(Subtraction(a, b), Addition(a, -Symbol(b)))
        self.assertEqual(Subtraction(a, b), Subtraction(-Symbol(b), -Symbol(a)))

    @given(*[valid_num_sym] * 3)
    def test__neq__(self, a, b, c):
        self.assertNotEqual(Subtraction(a, b), Symbol(c))
        if a != b:
            self.assertNotEqual(Subtraction(a, b), Subtraction(b, a))

    @given(*[valid_num_sym] * 4)
    def test__add__(self, a, b, c, d):
        if len(set([a, b, c, d])) != 4:
            return
        self.assertIsInstance(Subtraction(a, b) + Subtraction(c, d), Addition)

        self.assertIsInstance(Subtraction(a, b) + Symbol(c), Addition)
        self.assertIsInstance(Symbol(a) + Subtraction(b, c), Addition)

    @given(*[valid_num_sym] * 4)
    def test__sub__(self, a, b, c, d):
        if len(set([a, b, c, d])) != 4:
            return
        self.assertIsInstance(Subtraction(a, b) - Subtraction(c, d),
                Subtraction)

        self.assertIsInstance(Subtraction(a, b) - Symbol(c), Subtraction)
        self.assertIsInstance(Symbol(a) - Subtraction(b, c), Subtraction)
