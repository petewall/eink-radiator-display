#!/usr/bin/env python
# pylint: disable=no-value-for-parameter,import-outside-toplevel

import os
import click
from PIL import Image
from configuration import Configuration
from screen import Screen

@click.group()
def cli():
    pass

@cli.command()
def version():
    with open('./version', 'r', encoding='utf-8') as version_file:
        print(version_file.readline().strip())

@cli.command()
@click.option('--config', type=click.File('r'), required=False, help='Config file for the screen')
@click.argument('image', required=True)
def display(config, image):
    """ Display an image on the screen """
    if os.environ.get('EINK_SCREEN_PRESENT'):
        from inky_screen import InkyScreen
        screen = InkyScreen()
    else:
        config = Configuration(config)
        screen = Screen(config.palette())
    screen.set_image(Image.open(image))

if __name__ == '__main__':
    cli()
