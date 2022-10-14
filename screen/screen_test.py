import unittest
from test.pillow_image_matcher import the_same_image_as
from hamcrest import assert_that, is_
from PIL import Image
from screen.screen import Screen

class ScreenTest(unittest.TestCase):
    def test_set_color_palette_quantizes_wrb(self):
        screen = Screen(400, 300, ['white', 'red', 'black'])

        with Image.open('test/pencils.jpg') as image:
            quantized = screen.set_color_palette(image)
            # quantized.save('test/pencils_wrb.png')
            with Image.open('test/pencils_wrb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

    def test_set_color_palette_quantizes_wrbgb(self):
        screen = Screen(400, 300, ['white', 'red', 'black', 'green', 'blue'])

        with Image.open('test/pencils.jpg') as image:
            quantized = screen.set_color_palette(image)
            # quantized.save('test/pencils_wrbgb.png')
            with Image.open('test/pencils_wrbgb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))

    def test_set_color_palette_flattens_transparent_images(self):
        screen = Screen(400, 300, ['white', 'red', 'black', 'green', 'blue'])

        with Image.open('test/mango.png') as image:
            quantized = screen.set_color_palette(image)
            # quantized.save('test/mango_wrbgb.png')
            with Image.open('test/mango_wrbgb.png') as expected:
                assert_that(quantized, is_(the_same_image_as(expected)))
