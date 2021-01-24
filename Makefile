SHELL=/bin/bash

build: clean install test

clean:
	rm -rf .cache .pytest_cache coverage .coverage src/build src/vendor src/local.py venv

install:
	pip install pipenv
	pipenv install --dev
	pipenv run pre-commit install

lint: clean
	MYPYPATH=stubs pipenv run mypy
	PYTHONPATH=src pipenv run prospector

test:
	PYTHONPATH=src pipenv run pytest \
	--cov=src \
	--cov-fail-under=80 \
	--cov-report=html:coverage/html \
	tests

local:
	$(shell .scripts/local.sh)

ci-clean:
	rm -rf venv

ci-install:
	virtualenv -p python3 venv
	venv/bin/pip install -r src/requirements.txt --pre
	venv/bin/pip install -r tests/requirements.txt --pre

ci-lint:
	MYPYPATH=stubs venv/bin/mypy
	venv/bin/prospector

ci-test:
	PYTHONPATH=src venv/bin/pytest --fulltrace \
	--html=coverage/reports/report.xml \
	--self-contained-html \
	--cov=src \
	--cov-report term-missing \
	--cov-report=xml:coverage/coverage.xml \
	--cov-report=html:coverage/html \
	--junitxml=coverage/junit.xml \
	tests

ci:	ci-clean ci-install ci-lint ci-test
