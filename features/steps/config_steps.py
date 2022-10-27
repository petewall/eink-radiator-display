# pylint: disable=function-redefined,missing-function-docstring,subprocess-run-check

"""Steps related to the config command"""

import json
import subprocess
from behave import when, then # pylint: disable=no-name-in-module
from hamcrest import assert_that, equal_to, is_

@when('running the config command')
def step_impl(context):
    context.process = subprocess.run(['pipenv', 'run', 'python', 'main.py', 'config'], capture_output=True, text=True)

@then('the screen configuration for a UI screen is printed')
def step_impl(context):
    config = json.loads(str(context.process.stdout))
    assert_that(config['kind'], is_(equal_to('UI')))
    assert_that(config['size']['height'], is_(equal_to(480)))
    assert_that(config['size']['width'], is_(equal_to(640)))
    assert_that(config['palette'], is_(equal_to(['white', 'black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple'])))

@then('the screen configuration for an Inky wHAT Red screen is printed')
def step_impl(context):
    config = json.loads(str(context.process.stdout))
    assert_that(config['kind'], is_(equal_to('Inky wHAT red')))
    assert_that(config['size']['height'], is_(equal_to(300)))
    assert_that(config['size']['width'], is_(equal_to(400)))
    assert_that(config['palette'], is_(equal_to(['white', 'black', 'red'])))
