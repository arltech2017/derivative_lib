#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import unittest
from hypothesis import given, reproduce_failure
from hypothesis import strategies as st
import string

from derivative_lib import Symbol

__appname__     = "symbol"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


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


class _Arithmetic(unittest.TestCase):
    valid_symbol = st.text(string.ascii_letters, min_size=1)

    @given(*[valid_symbol] * 2)
    def test__add__(self, a, b):
        Symbol(a) + Symbol(b)

    @given(*[valid_symbol] * 2)
    def test__sub__(self, a, b):
        Symbol(a) - Symbol(b)

    @given(*[valid_symbol] * 2)
    def test__mul__(self, a, b):
        Symbol(a) * Symbol(b)

    @given(*[valid_symbol] * 2)
    def test__truediv__(self, a, b):
        Symbol(a) * Symbol(b)

    @given(*[valid_symbol] * 2)
    def test__truediv__(self, a, b):
        Symbol(a) / Symbol(b)

    @given(*[valid_symbol] * 2)
    def test__pow__(self, a, b):
        Symbol(a) ** Symbol(b)
