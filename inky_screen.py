# pylint: disable=import-error
from inky.auto import auto
from screen import Screen

class InkyScreen(Screen):
    def __init__(self, palette):
        physical_screen = auto()

        super().__init__(palette)
        self.hardware = physical_screen

    def show_image(self, image):
        self.hardware.set_image(image)
        self.hardware.show()
