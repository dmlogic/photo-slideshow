#!/usr/bin/env python3

import os.path
import time
from decimal import *
import config as cfg
from src import lookup
from src import display

imageLookup = lookup.Lookup(cfg.dbPath, cfg.photoPath)
imageDisplay = display.Display(cfg.max_width, cfg.max_height)

def display_image():
    nextImage = imageLookup.random_image()
    if os.path.isfile(nextImage['path']) :
        imageDisplay.send_to_hdmi(nextImage)
        time.sleep(cfg.imageDuration)
    else:
        display_image()

try:
    while True:
        display_image()
except KeyboardInterrupt:
    print('Finished!')

