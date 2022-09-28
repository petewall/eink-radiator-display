import unittest
from unittest.mock import MagicMock
from test.pillow_image_matcher import the_same_image_as
from hamcrest import assert_that, is_

from PIL import Image

from palette import make_palette
from screen import Screen

class ScreenTest(unittest.TestCase):
    def test_set_image_quantizes_wrb(self):
        screen = Screen(400, 300, make_palette(['white', 'red', 'black']))
        screen.show_image = MagicMock()

        with Image.open('test/pencils.jpg') as image:
            screen.set_image(image)
            assert_that(screen.show_image.called, is_(True))
            quantized = screen.show_image.call_args.args[0]
            # quantized.save('test/pencils_wrb.png')
            with Image.open('test/pencils_wrb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

    def test_set_image_quantizes_wrbgb(self):
        screen = Screen(400, 300, make_palette(['white', 'red', 'black', 'green', 'blue']))
        screen.show_image = MagicMock()

        with Image.open('test/pencils.jpg') as image:
            screen.set_image(image)
            assert_that(screen.show_image.called, is_(True))
            quantized = screen.show_image.call_args.args[0]
            # quantized.save('test/pencils_wrbgb.png')
            with Image.open('test/pencils_wrbgb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

    def test_set_image_flattens_transparent_images(self):
        screen = Screen(400, 300, make_palette(['white', 'red', 'black', 'green', 'blue']))
        screen.show_image = MagicMock()

        with Image.open('test/mango.png') as image:
            screen.set_image(image)
            assert_that(screen.show_image.called, is_(True))
            quantized = screen.show_image.call_args.args[0]
            # quantized.save('test/mango_wrbgb.png')
            with Image.open('test/mango_wrbgb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))
