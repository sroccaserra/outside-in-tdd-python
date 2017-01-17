
.PHONY: test
.DEFAULT_GOAL := test-all

clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

coverage:
	pytest --cov=app test feature

env:
	pyenv install -s 3.4.5
	pyenv local 3.4.5

lint:
	flake8 app test application.py

run:
	python -m application

test:
	pytest test

test-all:
	pytest test feature

