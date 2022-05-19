#!/usr/bin/env python3

import os.path
import sqlite3
import time
import pygame
from decimal import *
import config as cfg

database = sqlite3.connect(cfg.dbPath)

def send_image_to_hdmi(filename):
    try:
        image = pygame.image.load(filename)
        size = image.get_rect()
        width = size[2]
        height = size[3]
        if width > cfg.max_width:
             height = height * (Decimal(cfg.max_width)/Decimal(width))
             width = cfg.max_width
             image = pygame.transform.scale(image,(width,height))
        if height > cfg.max_height:
             width = width * (Decimal(cfg.max_height)/Decimal(height))
             height = cfg.max_height
             image = pygame.transform.scale(image,(width,height))
        windowSurfaceObj = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
        windowSurfaceObj.blit(image,(0,0))
        pygame.mouse.set_visible(0)
        pygame.display.update()
    except:
        print( "Bad image")
        print( filename)
        quit()

def get_image():
    query = database.cursor()
    row = query.execute('SELECT a.id as album_id, p.google_id, p.title FROM photos p JOIN albums a ON a.id = p.album_id ORDER BY RANDOM() LIMIT 1').fetchone();
    return cfg.photoPath+str(row[0])+'/'+str(row[1])+'.jpg';

def display_image():
    nextImage = get_image()
    if os.path.isfile(nextImage) :
        send_image_to_hdmi(nextImage)
        time.sleep(cfg.imageDuration)
    else:
        display_image()

try:
    while True:
        display_image()
except KeyboardInterrupt:
    print('Finished!')

