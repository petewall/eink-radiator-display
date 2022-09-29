# pylint: disable=invalid-name

from PIL import Image

class InkyWHAT():
    def __init__(self, color):
        self.colour = color
        self.HEIGHT = 300
        self.WIDTH = 400

    def set_image(self, image: Image):
        pass

    def show(self):
        pass

def auto():
    return InkyWHAT('red')
