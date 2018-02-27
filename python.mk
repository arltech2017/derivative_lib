VENV ?= venv
REQS ?= requirements.txt

.DELETE_ON_ERROR: $(VENV)
$(VENV):
	virtualenv $@

.PHONY: $(REQS)
$(REQS): $(VENV)
	$(VENV)/bin/pip install -r $@
