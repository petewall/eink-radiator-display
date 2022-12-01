"""Screen tests"""

import os
import unittest
from unittest.mock import MagicMock
from test.pillow_image_matcher import the_same_image_as
from hamcrest import assert_that, equal_to, is_
from PIL import Image
from screen.screen import Screen

class ScreenTest(unittest.TestCase):
    """Screen tests"""

    def test_set_color_palette_quantizes_wrb(self):
        """Tests quantizing an image with wrb palette"""
        screen = Screen('Test Screen', 400, 300, ['white', 'red', 'black'])

        with Image.open('test/pencils.jpg') as image:
            quantized = screen.set_color_palette(image)
            if os.getenv('GENERATE_TEST_ARTIFACTS') is not None:
                quantized.save('test/pencils_wrb.png')
            with Image.open('test/pencils_wrb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

    def test_set_color_palette_quantizes_wrbgb(self):
        """Tests quantizing an image with wrbgb palette"""
        screen = Screen('Test Screen', 400, 300, ['black', 'white', 'red', 'green', 'blue'])

        with Image.open('test/pencils.jpg') as image:
            quantized = screen.set_color_palette(image)
            if os.getenv('GENERATE_TEST_ARTIFACTS') is not None:
                quantized.save('test/pencils_bwrgb.png')
            with Image.open('test/pencils_bwrgb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

    def test_set_color_palette_flattens_transparent_images(self):
        """Tests quantizing a transparent image will flatten the image"""
        screen = Screen('Test Screen', 400, 300, ['black', 'white', 'red', 'green', 'blue'])

        with Image.open('test/mango.png') as image:
            quantized = screen.set_color_palette(image)
            if os.getenv('GENERATE_TEST_ARTIFACTS') is not None:
                quantized.save('test/mango_bwrgb.png')
            with Image.open('test/mango_bwrgb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

    def test_set_image(self):
        """Tests setting an image"""
        screen = Screen('Test Screen', 400, 300, ['black', 'white', 'red', 'green', 'blue'])
        screen.show_image = MagicMock()

        with Image.open('test/pencils.jpg') as image:
            screen.set_image(image)
            assert_that(screen.show_image.call_count, is_(equal_to(1)))
            args, _ = screen.show_image.call_args
            quantized = args[0]

            with Image.open('test/pencils_bwrgb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

    def test_set_image_with_output_file(self):
        """Tests that setting an image with an output file will save the quantized image to that file"""
        screen = Screen('Test Screen', 400, 300, ['black', 'white', 'red', 'green', 'blue'])
        screen.set_output_file('output.png')
        screen.show_image = MagicMock()

        with Image.open('test/pencils.jpg') as image:
            screen.set_image(image)
            assert_that(screen.show_image.call_count, is_(equal_to(1)))
            args, _ = screen.show_image.call_args
            quantized = args[0]

            with Image.open('test/pencils_bwrgb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

                with Image.open('output.png') as saved_image:
                    assert_that(saved_image, is_(the_same_image_as(expected)))
                    os.remove('output.png')
