#!/usr/bin/env python
# pylint: disable=no-value-for-parameter

from os import read
import readline
import click
from PIL import Image
from configuration import Configuration
from screen import Screen

@click.group()
def cli():
    pass

@cli.command()
def version():
    with open('./version', 'r') as version_file:
        print(version_file.readline().strip())

@cli.command()
@click.option("--config", type=click.File('r'), required=True, help="Config file for the screen")
@click.argument("image", required=True)
def display(config, image):
    """ Display an image on the screen """
    config = Configuration(config)
    screen = Screen(config.size, config.palette())
    screen.set_image(Image.open(image))

if __name__ == '__main__':
    cli()
