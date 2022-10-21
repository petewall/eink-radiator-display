# pylint: disable=function-redefined,subprocess-run-check

import os
from behave import given, then # pylint: disable=no-name-in-module
from hamcrest import assert_that, equal_to, is_

@given('the environment variable {key} is set to {value}')
def step_impl(_, key, value):
    os.environ[key] = value

@then('the command completes successfully')
def step_impl(context):
    assert_that(context.process.returncode, is_(equal_to(0)))

@then('the command returns an error')
def step_impl(context):
    assert_that(context.process.returncode, is_(equal_to(1)))
