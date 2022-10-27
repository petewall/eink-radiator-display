"""InkyScreen allows the use of Inky eInk screens from Pimoroni"""

from PIL import Image
from screen.screen import Screen

try:
    from inky import auto, InkyWHAT
except ModuleNotFoundError:
    # pylint: disable=ungrouped-imports
    from screen.mock_inky import auto, InkyWHAT

class InkyScreen(Screen):
    """InkyScreen allows the use of Inky eInk screens from Pimoroni"""
    def __init__(self, screen_type, color):
        if screen_type == 'what':
            physical_screen = InkyWHAT(color)
            kind = 'Inky wHAT ' + color
            colors = ['white', 'black', color]
        else:
            physical_screen = auto()
            kind = 'Inky something'
            colors = ['white', 'black']

        super().__init__(kind, physical_screen.HEIGHT, physical_screen.WIDTH, colors)
        self.hardware = physical_screen

    def show_image(self, image: Image):
        """Display the image on the Inky screen"""
        self.hardware.set_image(image)
        self.hardware.show()
