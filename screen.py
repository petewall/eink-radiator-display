from time import sleep

from PIL import Image

class Screen():
    def __init__(self, palette):
        self.palette = palette

    def set_image(self, image: Image):
        if image.mode == 'RGBA':
            background = Image.new('RGB', image.size, 'white')
            background.paste(image, mask=image.split()[3])
            image = background

        if image.mode == 'RGB':
            palette = Image.new('P', (16, 16))
            palette.putpalette(self.palette)
            image = image.quantize(palette=palette, dither=0)

        self.show_image(image)

    def show_image(self, _):
        sleep(0)
