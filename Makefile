SRCDIR  ?= src
TESTDIR ?= tests

TESTS   := $(shell find $(TESTDIR) -type f -name '*.py')

.IGNORE: test
test:
	PYTHONPATH=$(SRCDIR) python3 -m unittest -v $(TESTS)
