#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import copy

__appname__     = "utils"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

class UnorderedList(list):
    def __eq__(self, other):
        if super().__eq__(other) is True:  # stupid notimplemented evaluating to true
            return True
        if len(self) != len(other):
            return False
        other = other.copy()
        for item in self:
            if item not in other:
                return False
            other.remove(item)
        return not other

    def __neq__(self, other):
        return not self == other
