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
        self.assertIsInstance(Symbol(a) + Symbol(b), Addition)


class _Addition(unittest.TestCase):

    valid_symbols = st.text(string.ascii_letters, min_size=1)

    @given(*[valid_symbols] * 2)
    def test__init__(self, a, b):
        Addition(a, b)

    @given(*[valid_symbols] * 2)
    def test__str__(self, a, b):
        self.assertEqual(str(a) + ' + ' + str(b), str(Addition(a, b)))

    @given(*[valid_symbols] * 2)
    def test__eq__(self, a, b):
        self.assertEqual(Addition(a, b), Addition(a, b))

        self.assertEqual(Addition(a, b), Symbol(a))

        self.assertEqual(Addition(a, b), Addition(b, a))  # x + y == y + x

    @given(*[valid_symbols] * 4)
    def test__add__(self, a, b, c, d):
        self.assertIsInstance(Addition(a, b) + Addition(c, d), Addition)

        self.assertIsInstance(Addition(a, b) + Symbol(c), Addition)
        self.assertIsInstance(Symbol(a) + Addition(b, c), Addition)
