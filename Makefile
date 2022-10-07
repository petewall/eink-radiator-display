.PHONY: deps lint test test-units

clean:
	rm -rf temp

HAS_PIPENV := $(shell command -v pipenv;)

Pipfile.lock: Pipfile
	pipenv lock

temp/make-targets/deps: Pipfile.lock
ifndef HAS_PIPENV
	pip install pipenv
endif
	pipenv sync --dev
	mkdir -p temp/make-targets
	touch temp/make-targets/deps

deps: temp/make-targets/deps

build: # no-op

TEST_SOURCES := $(shell find $$PWD -name '*_test.py')
test-units: $(TEST_SOURCES) deps
	pipenv run python -m unittest $(TEST_SOURCES)

test: lint test-units

lint: temp/make-targets/deps
	pipenv run pylint \
		--disable line-too-long,missing-module-docstring,missing-class-docstring,missing-function-docstring\
		*.py

requirements.txt: Pipfile Pipfile.lock
	pipenv requirements > requirements.txt
	echo 'inky' >> requirements.txt
	echo 'rpi.gpio' >> requirements.txt

version.py:
	echo "version_number = \"$$(cat version)\"" > version.py
