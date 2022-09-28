from inky import auto, InkyWHAT
from palette import make_palette
from screen import Screen

class InkyScreen(Screen):
    def __init__(self, screen_type, color):
        if screen_type == "what":
            physical_screen = InkyWHAT(color)
            palette = make_palette(['black', 'white', color])
        else:
            physical_screen = auto()
            palette = make_palette([])

        super().__init__(physical_screen.HEIGHT, physical_screen.WIDTH, palette)
        self.hardware = physical_screen

    def show_image(self, image):
        self.hardware.set_image(image)
        self.hardware.show()
