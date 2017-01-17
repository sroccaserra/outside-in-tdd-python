
.PHONY: test
.DEFAULT_GOAL := test-all

clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

coverage:
	pytest --cov=domain --cov=infrastructure test

env:
	pyenv install -s 3.4.5
	pyenv local 3.4.5

lint:
	flake8 domain infrastructure test application.py

run:
	python -m application

test:
	pytest test/domain test/infrastructure

test-feature:
	pytest test/feature

test-all:
	pytest test

