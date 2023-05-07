#!/usr/bin/env python3

import os.path
import time
from decimal import *
import config as cfg
from src import lookup
from src import display

image_lookup = lookup.Lookup(cfg.db_path, cfg.photo_path)
image_display = display.Display(cfg.max_width, cfg.max_height, os.path.dirname(os.path.realpath(__file__))+'/fonts/')


def display_image():
    next_image = image_lookup.random_image()
    if os.path.isfile(next_image['path']):
        image_display.send_to_hdmi(next_image)
        time.sleep(cfg.image_duration)
    else:
        display_image()

try:
    while True:
        display_image()
except KeyboardInterrupt:
    print('Finished!')
