"""A mock implementation of the Inky module"""

from PIL import Image

class InkyWHAT():
    """A mock implementation of the Inky module"""

    def __init__(self, color):
        self.colour = color

        # pylint: disable=invalid-name
        self.HEIGHT = 300
        self.WIDTH = 400

    def set_image(self, image: Image):
        """noop"""

    def show(self):
        """noop"""

def auto():
    """Always returns an InkyWHAT Red"""
    return InkyWHAT('red')
