from inky.auto import auto
from configuration import make_palette
from screen import Screen

class InkyScreen(Screen):
    def __init__(self):
        physical_screen = auto()

        if physical_screen.colour == 'black':
            palette = make_palette(['white', 'black'])
        elif physical_screen.colour == 'red':
            palette = make_palette(['white', 'red', 'black'])
        elif physical_screen.colour == 'yellow':
            palette = make_palette(['white', 'yellow', 'black'])
        elif physical_screen.colour == '7colour':
            palette = make_palette(['white', 'red', 'green', 'blue', 'yellow', 'orange', 'black'])

        super().__init__(palette)
        self.hardware = physical_screen

    def show_image(self, image):
        self.hardware.set_image(image)
        self.hardware.show()
