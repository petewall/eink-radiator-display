#!/usr/bin/env python
# pylint: disable=no-value-for-parameter,import-outside-toplevel

import click
from PIL import Image
from inky_screen import InkyScreen

@click.group()
def cli():
    pass

@cli.command()
def version():
    with open('./version', 'r', encoding='utf-8') as version_file:
        print(version_file.readline().strip())

@cli.command()
# @click.option('--screen-type', type=click.File('t'), required=False, help='Type of the Inky screen ')
# @click.option('--screen-color', type=click.File('c'), required=False, help='Color of the Inky screen ')
@click.argument('image', required=True)
def display(image):
    """ Display an image on the screen """
    screen = InkyScreen("what", "red")
    screen.set_image(Image.open(image))

if __name__ == '__main__':
    cli()
