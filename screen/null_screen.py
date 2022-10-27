"""NullScreen does nothing"""

from PIL import Image
from screen.screen import Screen

class NullScreen(Screen):
    """NullScreen does nothing"""

    def __init__(self):
        height = 480
        width = 640
        colors = ['white', 'black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']
        super().__init__('Null', height, width, colors)

    def show_image(self, image: Image):
        """noop"""
