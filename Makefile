# Makefile
SHELL = /bin/bash

# Handles help functionality
.PHONY: help
help:
	@echo "Commands:"
	@echo "venv    : creates a virtual environment."
	@echo "style   : executes style formatting."
	@echo "clean   : cleans all unnecessary files."
	@echo "test    : execute tests on code, data and models."

# Styling
.PHONY: style
style:
    black .
    flake8
    python3 -m isort .

# Cleaning; style is pre-requisite to clean
.PHONY: clean
clean: style
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E ".trash" | xargs rm -rf
	rm -f .coverage

# Environment; ensure all commands are run in the same shell 
# .ONESHELL: # if `&&` is not used
venv:
    python3 -m venv venv
    source venv/bin/activate && \
    python3 -m pip install pip setuptools wheel && \
    python3 -m pip install -e .

# Test; will include testing schemas for GE
.PHONY: test
test:
    pytest -m "not training"
    cd tests && great_expectations checkpoint run projects
    cd tests && great_expectations checkpoint run tags
    cd tests && great_expectations checkpoint run labeled_projects