SRCDIR  ?= src
TESTDIR ?= tests

SRCS    := $(shell find $(SRCDIR)  -type f -name '*.py')
TESTS   := $(shell find $(TESTDIR) -type f -name '*.py')

export PYTHONPATH=$(abspath $(SRCDIR))
REQS=requirements.txt $(TESTDIR)/requirements.txt
include python.mk
export PATH := $(VENV)/bin:$(PATH)

.DEFAULT_GOAL := mytarget

.IGNORE: test
test: test_syntax $(TESTDIR)/requirements.txt
	python3 -m unittest -v $(TESTS)

.IGNORE: test_syntax 
test_syntax: $(TESTDIR)/requirements.txt
	pycodestyle $(SRCS)

