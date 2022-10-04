from PIL import Image
from screen import Screen

try:
    from inky import auto, InkyWHAT
except ModuleNotFoundError:
    from mock_inky import auto, InkyWHAT

class InkyScreen(Screen):
    def __init__(self, screen_type, color):
        if screen_type == "what":
            physical_screen = InkyWHAT(color)
            colors = ['black', 'white', color]
        else:
            physical_screen = auto()
            colors = ['black', 'white']

        super().__init__(physical_screen.HEIGHT, physical_screen.WIDTH, colors)
        self.hardware = physical_screen

    def show_image(self, image: Image):
        self.hardware.set_image(image)
        self.hardware.show()
