from PIL import Image
from screen import Screen

class UIScreen(Screen):
    def __init__(self):
        height = 480
        width = 640
        colors = ["black", "white", "red", "green", "blue"]
        super().__init__(height, width, colors)

    def show_image(self, image: Image):
        image.show()
