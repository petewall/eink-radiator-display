.PHONY: deps lint test test-units

clean:
	rm -rf temp

HAS_PIPENV := $(shell command -v pipenv;)

Pipfile.lock: Pipfile
	pipenv lock

temp/make-targets/deps: Pipfile.lock
ifndef HAS_PIPENV
	$(error "pipenv is required")
endif
	pipenv sync --dev
	mkdir -p temp/make-targets
	touch temp/make-targets/deps

deps: temp/make-targets/deps

TEST_SOURCES := $(shell find $$PWD -name '*_test.py')
test-units: $(TEST_SOURCES) deps
	pipenv run python -m unittest $(TEST_SOURCES)

# test-features: deps
# 	pipenv run behave

test: lint test-units

lint: temp/make-targets/deps
	pipenv run pylint \
		--disable line-too-long,missing-module-docstring,missing-class-docstring,missing-function-docstring\
		*.py
