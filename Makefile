SRCDIR  ?= src
TESTDIR ?= tests

SRCS    := $(shell find $(SRCDIR)  -type f -name '*.py')
TESTS   := $(shell find $(TESTDIR) -type f -name '*.py')

export PYTHONPATH=$(abspath $(SRCDIR))
REQS=requirements.txt $(TESTDIR)/requirements.txt
include python.mk

.DEFAULT_GOAL := test

.IGNORE: test
test: test_syntax $(TESTDIR)/requirements.txt
	python3 -m unittest -v $(TESTS)

.IGNORE: test_syntax 
test_syntax: $(TESTDIR)/requirements.txt
	pycodestyle $(SRCS)

