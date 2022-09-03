import unittest
from hamcrest import assert_that, calling, equal_to, raises
import yaml

from configuration import make_palette, percent_to_absolute, Configuration

class MakePaletteTest(unittest.TestCase):
    def test_make_palette(self):
        palette = make_palette(['red', 'blue', 'green', 'white'])
        assert_that(len(palette), equal_to(256*3))
        assert_that(palette[0:3], equal_to((255, 0, 0)))        # Red
        assert_that(palette[3:6], equal_to((0, 0, 255)))        # Blue
        assert_that(palette[6:9], equal_to((0, 128, 0)))        # Green
        assert_that(palette[9:12], equal_to((255, 255, 255)))   # White

        i = 12
        while i < len(palette):
            assert_that(palette[i], equal_to(0))
            i += 1

class PercentToAbsoluteTest(unittest.TestCase):
    def test_zero(self):
        assert_that(percent_to_absolute(0.0), equal_to(0))

    def test_half(self):
        assert_that(percent_to_absolute(0.5), equal_to(127))

    def test_one(self):
        assert_that(percent_to_absolute(1.0), equal_to(255))

    def test_negative(self):
        assert_that(calling(percent_to_absolute).with_args(-1.0), raises(Exception, 'color value must be between 0 and 1'))

    def test_over_one(self):
        assert_that(calling(percent_to_absolute).with_args(2.0), raises(Exception, 'color value must be between 0 and 1'))


class ConfigurationTest(unittest.TestCase):
    def test_constructor(self):
        config_data = yaml.dump({
            'size': {
                'width': 640,
                'height': 480
            },
            'colors': [
                'red', 'blue', 'green', 'white'
            ]
        })
        config = Configuration(config_data)
        assert_that(config.size, equal_to((640, 480)))

    def test_constructor_none_raises(self):
        assert_that(calling(Configuration).with_args(None), raises(Exception, 'config file is not readable'))

    def test_constructor_not_yaml_raises(self):
        pass
        # assert_that(calling(Configuration).with_args('-- this is !! not !@#" YAML'), raises(Exception, 'config file is not readable'))

    def test_constructor_empty_string_raises(self):
        assert_that(calling(Configuration).with_args(''), raises(Exception, 'the config file is missing the screen size'))

    def test_constructor_missing_height_raises(self):
        config_data = yaml.dump({
            'size': {
                'width': 640,
            },
            'colors': [
                'red', 'blue', 'green', 'white'
            ]
        })
        assert_that(calling(Configuration).with_args(config_data), raises(Exception, 'the config file is missing the screen height'))

    def test_constructor_missing_width_raises(self):
        config_data = yaml.dump({
            'size': {
                'hight': 480,
            },
            'colors': [
                'red', 'blue', 'green', 'white'
            ]
        })
        assert_that(calling(Configuration).with_args(config_data), raises(Exception, 'the config file is missing the screen width'))

    def test_constructor_missing_colors_raises(self):
        config_data = yaml.dump({
            'size': {
                'width': 640,
                'height': 480,
            }
        })
        assert_that(calling(Configuration).with_args(config_data), raises(Exception, 'the config file is missing the screen colors'))

    def test_constructor_empty_colors_raises(self):
        config_data = yaml.dump({
            'size': {
                'width': 640,
                'height': 480,
            },
            'colors': []
        })
        assert_that(calling(Configuration).with_args(config_data), raises(Exception, 'the config file is missing the screen colors'))

    def test_palette_generation(self):
        config_data = yaml.dump({
            'size': {
                'width': 640,
                'height': 480
            },
            'colors': [
                'red', 'blue', 'green', 'white'
            ]
        })
        config = Configuration(config_data)
        palette = config.palette()
        assert_that(len(palette), equal_to(256*3))
        assert_that(palette[0:3], equal_to((255, 0, 0)))        # Red
        assert_that(palette[3:6], equal_to((0, 0, 255)))        # Blue
        assert_that(palette[6:9], equal_to((0, 128, 0)))        # Green
        assert_that(palette[9:12], equal_to((255, 255, 255)))   # White

        i = 12
        while i < len(palette):
            assert_that(palette[i], equal_to(0))
            i += 1

if __name__ == '__main__':
    unittest.main()
