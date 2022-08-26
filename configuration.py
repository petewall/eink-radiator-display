# pylint: disable=too-few-public-methods

from colour import Color
import yaml

def percent_to_absolute(color_value):
    """Convert from percent (0.0 - 1.0) to absolute value (0 - 255)"""
    return int(color_value*255)

class Configuration():
    def __init__(self, config_data):
        config = None
        try:
            config = yaml.safe_load(config_data)
        except yaml.YAMLError as yaml_exception:
            raise Exception('unable to parse config file: ' + str(yaml_exception)) from yaml_exception

        if 'size' not in config:
            raise Exception('the config file is missing the screen size')
        if 'width' not in config['size']:
            raise Exception('the config file is missing the screen width')
        if 'height' not in config['size']:
            raise Exception('the config file is missing the screen height')
        self.size = (
            config['size']['width'],
            config['size']['height']
        )

        if 'colors' not in config or len(config['colors']) == 0:
            raise Exception('the config file is missing the screen colors')
        self.colors = config['colors']

    def palette(self):
        """Get the palette from the list of colors"""
        palette = ()
        for color in self.colors:
            palette += Color(color).rgb
        palette += (0, 0, 0) * (256 - len(self.colors))
        palette = tuple(map(percent_to_absolute, palette))
        return palette
