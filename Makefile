.PHONY: run test

run:
	PYTHONPATH=src python3 -m emulator

test:
	PYTHONPATH=src python3 -m pytest tests
