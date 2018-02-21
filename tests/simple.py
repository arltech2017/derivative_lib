#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import unittest

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
    def testPrintsTrue(self):
        import operator
        addition = Equation(2, operator.add, "{args[0]} - {args[1]}")
        self.assertEquals(Symbol(2), subtraction(Symbol(1), Symbol(1)))
