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
        "kind": screen.kind,
        "size": {
            "height": screen.height,
            "width": screen.width
        },
        "palette": screen.colors
    }))

@cli.command()
@click.argument('image', required=True)
@click.option('--save', type=str, required=False, help='Save the image displayed to the screen')
def display(image, save):
    """ Display an image on the screen """
    if save != "":
        screen.set_output_file(save)
    screen.set_image(Image.open(image))

if __name__ == '__main__':
    cli()
