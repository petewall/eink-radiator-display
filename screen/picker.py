from screen.inky_screen import InkyScreen
from screen.screen import Screen
from screen.ui_screen import UIScreen

def new_screen(screen_type: str) -> Screen:
    if screen_type == "inkywhat-red":
        return InkyScreen("what", "red")
    if screen_type == "inkywhat-yellow":
        return InkyScreen("what", "yellow")
    return UIScreen()
