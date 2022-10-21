# pylint: disable=function-redefined,subprocess-run-check

import os
import subprocess
from test.pillow_image_matcher import the_same_image_as
from behave import when, then # pylint: disable=no-name-in-module
from hamcrest import assert_that, contains_string, is_
from PIL import Image

@when('running the display command with the save arg')
def step_impl(context):
    context.process = subprocess.run(["pipenv", "run", "python", "main.py", "display", "test/mango.png", "--save", "output.png"], capture_output=True, text=True)

@when('running the display command with a missing file')
def step_impl(context):
    context.process = subprocess.run(["pipenv", "run", "python", "main.py", "display", "test/missing.png"], capture_output=True, text=True)

@then('a quantized version of the image is displayed')
def step_impl(_):
    with Image.open('output.png') as image:
        with Image.open('test/mango_bwrgb.png') as expected:
            assert_that(image, is_(the_same_image_as(expected)))
    os.remove('output.png')

@then('prints that the image file was not found')
def step_impl(context):
    assert_that(str(context.process.stderr), contains_string("No such file or directory: 'test/missing.png'"))
