"""This screen will open the image in the UI"""

from PIL import Image
from screen.screen import Screen

class UIScreen(Screen):
    """This screen will open the image in the UI"""

    def __init__(self):
        height = 480
        width = 640
        colors = ['white', 'black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']
        super().__init__('UI', height, width, colors)

    def show_image(self, image: Image):
        """Shows the image"""
        image.show()
