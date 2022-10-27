"""The screen picker is a factory function for creating screens"""

from screen.inky_screen import InkyScreen
from screen.null_screen import NullScreen
from screen.screen import Screen
from screen.ui_screen import UIScreen

def new_screen(screen_type: str) -> Screen:
    """Instantiate a screen object based on the screen type"""
    if screen_type == 'inkywhat-red':
        return InkyScreen('what', 'red')
    if screen_type == 'inkywhat-yellow':
        return InkyScreen('what', 'yellow')
    if screen_type == 'null':
        return NullScreen()
    if screen_type == 'ui':
        return UIScreen()
    raise ValueError(f'invalid screen type: {screen_type}')
