# pylint: disable=function-redefined,subprocess-run-check

import subprocess
from behave import when, then # pylint: disable=no-name-in-module
from hamcrest import assert_that, equal_to, is_

@when('running the version command')
def step_impl(context):
    context.process = subprocess.run(["./main.py", "version"], capture_output=True, text=True)

@then('command completes successfully')
def step_impl(context):
    assert_that(context.process.returncode, is_(equal_to(0)))

@then('the version number is printed')
def step_impl(context):
    assert_that(str(context.process.stdout), is_(equal_to("0.0.0\n")))
