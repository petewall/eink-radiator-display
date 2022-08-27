# pylint: disable=import-error
from inky.auto import auto
from screen import Screen

class InkyScreen(Screen):
    def __init__(self, palette):
        physical_screen = auto()

        super().__init__(physical_screen.resolution, palette)
        self.hardware = physical_screen

    def show_image(self):
        self.hardware.set_image(self.image)
        self.hardware.show()
