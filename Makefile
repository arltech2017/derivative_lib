test:
	PYTHONPATH=$$PWD/src python3 -m unittest discover tests/ -p '*.py'
