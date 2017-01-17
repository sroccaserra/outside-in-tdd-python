
.PHONY: test
.DEFAULT_GOAL := test-all

coverage:
	pytest --cov=app test feature

lint:
	flake8 app test
test:
	pytest test

test-all:
	pytest test feature

