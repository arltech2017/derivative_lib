#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from parse import parse
import readline

__appname__     = "__main__"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

while True:
    t = parse('({})'.format(input('> ')))
    print('{}\' = {}'.format(t, t.derivative().simplify()))
