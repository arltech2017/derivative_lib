#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

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


from __init__ import *


def tryToDigit(numeric_string):
    try:
        return float(numeric_string)
    except ValueError:
        return None


class Stack(list):
    def push(self, val):
        super().append(val)

class BinaryTree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def insertLeft(self, val):
        self.left = BinaryTree(val)
    def insertRight(self, val):
        self.right = BinaryTree(val)

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self, val):
        self.val = val

    def __repr__(self):
        return 'BinaryTree({}, leftchild: {}, rightchild: {})'.format(self.val, self.left, self.right)

    def simplify(self):
        if self.val == '':
            if (self.left is not None) ^ (self.right is not None):
                return (self.left or self.right).simplify()
        return self

def nospace_parse_decorator(func):
    return lambda fpexp: func(' '.join(re.findall('(\d+|[A-z]+|\*\*|[+-/*()])', fpexp)))

import operator
symbols = {'*': operator.mul, '**': operator.pow, '+': operator.add}

# FFrom interactive python book
@nospace_parse_decorator
def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent
        #elif i in ['+', '-', '*', '/']:
        elif i in symbols.keys():
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


import re


def translate(symbol):
    if symbol in symbols:
        return symbols[symbol]
    elif tryToDigit(symbol) is not None:
        return Number(tryToDigit(symbol))
    else:
        return Symbol(symbol)


def parseParseTree(binaryTree):
    op = translate(binaryTree.val)
    if binaryTree.left is not None and binaryTree.right is not None:
        return op(parseParseTree(binaryTree.left), parseParseTree(binaryTree.right))
    return op

def parse(expression):
    tree = buildParseTree(expression).simplify()
    return parseParseTree(tree)


import readline
while True:
    t = parse('({})'.format(input('> ')))
    print('{}\' = {}'.format(t, t.derivative()))
