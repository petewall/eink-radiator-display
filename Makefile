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

ALL_PYTHON_SOURCES := $(shell find $$PWD -name '*.py')

lint: $(ALL_PYTHON_SOURCES) deps
	pipenv run pylint \
		--disable line-too-long,missing-module-docstring,missing-class-docstring,missing-function-docstring\
		$(ALL_PYTHON_SOURCES)

TEST_SOURCES := $(shell find $$PWD -name '*_test.py')
test-units: $(TEST_SOURCES) deps
	pipenv run python -m unittest $(TEST_SOURCES)

FEATURE_SOURCES := $(shell find features -type f)
test-features: $(FEATURE_SOURCES) deps
	PIPENV_VERBOSITY=-1 pipenv run behave

test: test-units test-features

requirements.txt: Pipfile Pipfile.lock
	pipenv requirements > requirements.txt
	echo 'inky' >> requirements.txt
	echo 'rpi.gpio' >> requirements.txt

version.py:
	echo "VERSION_NUMBER = \"$$(cat version)\"" > version.py
