import unittest
from hamcrest import assert_that, calling, equal_to, raises
import yaml

from configuration import percent_to_absolute, Configuration

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
            'colors': {
                'red', 'blue', 'green', 'white'
            }
        })
        config = Configuration(config_data)
        assert_that(config.size, equal_to((640, 480)))

    def test_constructor_none_raises(self):
        assert_that(calling(Configuration).with_args(None), raises(Exception, 'config file is not readable'))

    def test_constructor_not_yamlraises(self):
        pass
        # assert_that(calling(Configuration).with_args('-- this is !! not !@#" YAML'), raises(Exception, 'config file is not readable'))

    def test_constructor_empty_stringraises(self):
        assert_that(calling(Configuration).with_args(''), raises(Exception, 'the config file is missing the screen size'))

    def test_constructor_missing_heightraises(self):
        config_data = yaml.dump({
            'size': {
                'width': 640,
            },
            'colors': {
                'red', 'blue', 'green', 'white'
            }
        })
        assert_that(calling(Configuration).with_args(config_data), raises(Exception, 'the config file is missing the screen height'))

    def test_constructor_missing_hidthraises(self):
        pass

    def test_constructor_missing_colorsraises(self):
        pass

    def test_constructor_empty_colorsraises(self):
        pass

    def test_palette_generation(self):
        pass

if __name__ == '__main__':
    unittest.main()
