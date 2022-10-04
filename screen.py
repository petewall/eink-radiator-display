from time import sleep

from PIL import Image

from palette import make_palette

class Screen():
    def __init__(self, height, width, colors):
        self.height = height
        self.width = width
        self.colors = colors
        self.palette = make_palette(colors)

    def set_color_palette(self, image: Image):
        if image.mode == 'RGBA':
            background = Image.new('RGB', image.size, 'white')
            background.paste(image, mask=image.split()[3])
            image = background

        if image.mode == 'RGB':
            palette = Image.new('P', (16, 16))
            palette.putpalette(self.palette)
            image = image.quantize(palette=palette, dither=0)

        return image

    def set_image(self, image: Image):
        image = self.set_color_palette(image)
        self.show_image(image)

    def show_image(self, _):
        sleep(0)
