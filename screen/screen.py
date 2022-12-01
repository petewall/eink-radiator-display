"""The Screen represents the user interface hardware that will display images"""

from PIL import Image

from palette import make_palette

class Screen():
    """The Screen represents the user interface hardware that will display images"""

    def __init__(self, kind, height, width, colors):
        self.kind = kind
        self.height = height
        self.width = width
        self.colors = colors
        self.output_file = ''
        self.palette = make_palette(colors)

    def set_color_palette(self, image: Image):
        """Setting the color palette of an image will flatten and quantize it"""
        if image.mode == 'RGBA':
            background = Image.new('RGB', image.size, 'white')
            background.paste(image, mask=image.split()[3])
            image = background

        if image.mode == 'RGB':
            palette = Image.new('P', (16, 16))
            palette.putpalette(self.palette)
            image = image.quantize(palette=palette, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)

        return image

    def set_output_file(self, output_file: str):
        """Setting the output file will save to that file when displaying"""
        self.output_file = output_file

    def set_image(self, image: Image):
        """Setting the image will quantize it with the palette and display it to the screen"""
        image = self.set_color_palette(image)

        if self.output_file != '':
            image.save(self.output_file)

        self.show_image(image)

    def show_image(self, _):
        """noop"""
