# pylint: disable=protected-access

from time import sleep

from PIL import Image

def quantize(image, palette):
    """Convert an RGB or L mode image to use a given P image's palette."""
    # From https://stackoverflow.com/a/29438149/1255644

    image.load()
    palette.load()
    if palette.mode != 'P':
        raise ValueError('bad mode for palette image')
    if image.mode not in ['RGB', 'L']:
        raise ValueError('only RGB or L mode images can be quantized to a palette')
    converted_image = image.im.convert('P', 0, palette.im)  # the 0 means turn OFF dithering

    return image._new(converted_image)


class Screen():
    def __init__(self, size, palette):
        self.image = None
        self.size = size
        self.palette = palette

    def set_image(self, image: Image):
        if image.mode == 'RGBA':
            background = Image.new('RGB', image.size, 'white')
            background.paste(image, mask=image.split()[3])
            image = background

        if image.mode == 'RGB':
            palette = Image.new('P', (16, 16))
            palette.putpalette(self.palette)
            image = quantize(image, palette)

        self.image = image
        self.show_image()

    def show_image(self):
        sleep(0)
