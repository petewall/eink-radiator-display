"""Palette tests"""

import unittest
from hamcrest import assert_that, calling, equal_to, raises

from palette import make_palette, percent_to_absolute

class MakePaletteTest(unittest.TestCase):
    """Tests the make_palette function"""

    def test_make_palette(self):
        """Tests making a palette from a list of colors"""
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
    """Tests the percent_to_absolute function"""
    def test_zero(self):
        """Tests that 0 becomes 0"""
        assert_that(percent_to_absolute(0.0), equal_to(0))

    def test_half(self):
        """Tests that 1/2 becomes 127"""
        assert_that(percent_to_absolute(0.5), equal_to(127))

    def test_one(self):
        """Tests that 1 becomes 255"""
        assert_that(percent_to_absolute(1.0), equal_to(255))

    def test_negative(self):
        """Tests that values below zero raise exceptions"""
        assert_that(calling(percent_to_absolute).with_args(-1.0), raises(ValueError, 'color value must be between 0 and 1'))

    def test_over_one(self):
        """Tests that values greater than one raise exceptions"""
        assert_that(calling(percent_to_absolute).with_args(2.0), raises(ValueError, 'color value must be between 0 and 1'))
