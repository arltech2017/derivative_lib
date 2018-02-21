#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import unittest
from hypothesis import given
from hypothesis import strategies as st

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


class Addition(unittest.TestCase):
    @given(st.integers(), st.integers())
    def testPrintsTrue(self, a, b):
        import operator
        addition = Equation(2, operator.add, "{args[0]} - {args[1]}")
        self.assertEquals(Symbol(a + b), addition(Symbol(a), Symbol(b)))
