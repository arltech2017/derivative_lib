SRCDIR  ?= src
TESTDIR ?= tests

SRCS    := $(shell find $(SRCDIR)  -type f -name '*.py')
TESTS   := $(shell find $(TESTDIR) -type f -name '*.py')

.IGNORE: test
test: test_syntax
	PYTHONPATH=$(SRCDIR) python3 -m unittest -v $(TESTS)

.IGNORE: test_syntax
test_syntax:
	pycodestyle -v $(SRCS)
