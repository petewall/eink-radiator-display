"""Functions for creating color palettes"""

from colour import Color

def make_palette(colors):
    """Make a color palette from a list of colors"""
    palette = ()
    for color in colors:
        palette += Color(color).rgb
    palette += (0, 0, 0) * (256 - len(colors))
    palette = tuple(map(percent_to_absolute, palette))
    return palette

def percent_to_absolute(color_value):
    """Convert from percent (0.0 - 1.0) to absolute value (0 - 255)"""
    if color_value < 0.0 or color_value > 1.0:
        raise ValueError('color value must be between 0 and 1')
    return int(color_value*255)
