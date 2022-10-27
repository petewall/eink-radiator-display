# pylint: disable=function-redefined,missing-function-docstring,subprocess-run-check

"""Steps related to the version command"""

import subprocess
from behave import when, then # pylint: disable=no-name-in-module
from hamcrest import assert_that, equal_to, is_

@when('running the version command')
def step_impl(context):
    context.process = subprocess.run(['pipenv', 'run', 'python', 'main.py', 'version'], capture_output=True, text=True)

@then('the version number is printed')
def step_impl(context):
    with open('version', encoding='utf-8') as version:
        assert_that(str(context.process.stdout), is_(equal_to(version.readline())))
