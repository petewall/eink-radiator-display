from PIL import Image
from screen.screen import Screen

class NullScreen(Screen):
    def __init__(self):
        height = 480
        width = 640
        colors = ["black", "white", "red", "green", "blue"]
        super().__init__("Null", height, width, colors)

    def show_image(self, image: Image):
        pass
