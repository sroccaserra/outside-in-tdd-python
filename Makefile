
.PHONY: test
.DEFAULT_GOAL := test-all

coverage:
	pytest --cov=app test feature

test:
	pytest test

test-all:
	pytest test feature

