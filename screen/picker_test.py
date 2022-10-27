"""Screen picker tests"""

import unittest
from hamcrest import assert_that, calling, equal_to, is_, raises
from screen.picker import new_screen

class ScreenPickerTest(unittest.TestCase):
    """Screen picker tests"""

    def test_inky_what_red_screen(self):
        """Tests inkywhat-red returns an Inky wHAT red screen"""
        screen = new_screen('inkywhat-red')
        assert_that(screen.kind, is_(equal_to('Inky wHAT red')))
        assert_that(screen.height, is_(equal_to(300)))
        assert_that(screen.width, is_(equal_to(400)))
        assert_that(screen.colors, is_(equal_to(['white', 'black', 'red'])))

    def test_inky_what_yellow_screen(self):
        """Tests inkywhat-yellow returns an Inky wHAT yellow screen"""
        screen = new_screen('inkywhat-yellow')
        assert_that(screen.kind, is_(equal_to('Inky wHAT yellow')))
        assert_that(screen.height, is_(equal_to(300)))
        assert_that(screen.width, is_(equal_to(400)))
        assert_that(screen.colors, is_(equal_to(['white', 'black', 'yellow'])))

    def test_ui_screen(self):
        """Tests ui returns an UI screen"""
        screen = new_screen('ui')
        assert_that(screen.kind, is_(equal_to('UI')))
        assert_that(screen.height, is_(equal_to(480)))
        assert_that(screen.width, is_(equal_to(640)))
        assert_that(screen.colors, is_(equal_to(['white', 'black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple'])))

    def test_null_screen(self):
        """Tests null returns a Null screen"""
        screen = new_screen('null')
        assert_that(screen.kind, is_(equal_to('Null')))
        assert_that(screen.height, is_(equal_to(480)))
        assert_that(screen.width, is_(equal_to(640)))
        assert_that(screen.colors, is_(equal_to(['white', 'black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple'])))

    def test_unknown_screen(self):
        """Tests an unknown input raises an error"""
        assert_that(calling(new_screen).with_args('something else'), raises(ValueError, 'invalid screen type: something else'))
