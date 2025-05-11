.PHONY: help install uninstall run venv freeze clean

VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

help:
	@echo "Available commands:"
	@echo "  make install     - Install Quack Docs CLI via pipx (requires pipx installed)"
	@echo "  make uninstall   - Uninstall Quack Docs CLI via pipx"
	@echo "  make venv        - Create a virtual environment (optional)"
	@echo "  make freeze      - Freeze dependencies to requirements.txt"
	@echo "  make clean       - Remove virtual environment"
	@echo "  make run         - Run the app locally (venv required)"

install:
	@echo "Installing Quack Docs CLI via pipx..."
	pipx install .

uninstall:
	@echo "Uninstalling Quack Docs CLI via pipx..."
	pipx uninstall quack-docs

venv:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "Virtual environment created at $(VENV_DIR)"

freeze:
	@echo "Generating requirements.txt..."
	$(PIP) freeze > requirements.txt

run:
	@echo "Running the application..."
	$(PYTHON) main.py

clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV_DIR)