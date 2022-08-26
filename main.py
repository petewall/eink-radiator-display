#!/usr/bin/env python
# pylint: disable=no-value-for-parameter

import click
from PIL import Image
from configuration import Configuration
from screen import Screen

@click.command()
@click.option("--config", type=click.File('r'), required=True, help="Config file for the screen")
@click.argument("image", required=True)
def display(config, image):
    """ Display an image on the screen """
    config = Configuration(config)
    screen = Screen(config.size, config.palette())
    screen.set_image(Image.open(image))

if __name__ == '__main__':
    display()
