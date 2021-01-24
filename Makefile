SHELL := /bin/bash

lint:
#--ignore-patterns set in .pylintrc
	pylint bin/*
.PHONY: lint

test:
	python -m unittest discover tests
	sh tests/test.sh
.PHONY: test
