#!/usr/bin/env python
# pylint: disable=no-value-for-parameter,import-outside-toplevel

import json
import os
import click
from PIL import Image
from screen.picker import new_screen
from version import version_number

screen_type = os.getenv("EINK_RADIATOR_SCREEN_TYPE", default="inkywhat-red")
screen = new_screen(screen_type)

@click.group()
def cli():
    pass

@cli.command()
def version():
    """ Print the version of this utility """
    print(version_number)

@cli.command()
def config():
    """ Print the screen configuration """
    print(json.dumps({
        "size": {
            "height": screen.height,
            "width": screen.width
        },
        "palette": screen.colors
    }))

@cli.command()
# @click.option('--screen-type', type=click.File('t'), required=False, help='Type of the Inky screen ')
# @click.option('--screen-color', type=click.File('c'), required=False, help='Color of the Inky screen ')
@click.argument('image', required=True)
def display(image):
    """ Display an image on the screen """
    screen.set_image(Image.open(image))

if __name__ == '__main__':
    cli()
