from time import sleep

from PIL import Image

from palette import make_palette

class Screen():
    def __init__(self, kind, height, width, colors):
        self.kind = kind
        self.height = height
        self.width = width
        self.colors = colors
        self.output_file = ""
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

    def set_output_file(self, output_file: str):
        self.output_file = output_file

    def set_image(self, image: Image):
        image = self.set_color_palette(image)

        if self.output_file != "":
            image.save(self.output_file)

        self.show_image(image)

    def show_image(self, _):
        sleep(0)
