
.PHONY: test
.DEFAULT_GOAL := test-all

env:
	pyenv install -s 3.4.5
	pyenv local 3.4.5

requirements:
	pip install -Ur requirements.txt

lint:
	flake8 domain infrastructure test application.py

test:
	pytest test/domain test/infrastructure

test-feature:
	pytest test/feature

test-all:
	pytest test

coverage:
	pytest --cov=domain --cov=infrastructure test

run:
	python -m application

clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

