VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
ACTIVATE = $(VENV_DIR)/bin/activate

.PHONY: help venv install run clean freeze activate deactivate

help:
	@echo "Available commands:"
	@echo "  make venv     - create a virtual environment"
	@echo "  make install  - install dependencies"
	@echo "  make run      - run the application"
	@echo "  make clean    - clean up the environment"
	@echo "  make freeze   - freeze dependencies to requirements.txt"

venv:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)

install: venv
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

freeze:
	@echo "Generating requirements.txt..."
	$(PIP) freeze > requirements.txt

run:
	@echo "Running the application..."
	$(PYTHON) main.py

clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV_DIR)