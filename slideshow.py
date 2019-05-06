#!/usr/bin/env python3

import os.path
import sqlite3
import time
import pygame
imageDuration = 5
# dbPath =  '/Users/darren/projects/photo_frame/photo-indexer/database/database.sqlite'
# photoPath = '/Users/darren/projects/photo_frame/photo-indexer/storage/photos/'
dbPath =  '/home/pi/photo-indexer/database/database.sqlite'
photoPath = '/home/pi/storage/photos/'
database = sqlite3.connect(dbPath)

def send_image_to_hdmi(filename):
    # print( filename )
    image = pygame.image.load(filename)
    size = image.get_rect()
    width = size[2]
    height = size[3]
    windowSurfaceObj = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
    windowSurfaceObj.blit(image,(0,0))
    pygame.display.update()

def get_image():
    query = database.cursor()
    row = query.execute('SELECT a.id as album_id, p.google_id, p.title FROM photos p JOIN albums a ON a.id = p.album_id ORDER BY RANDOM() LIMIT 1').fetchone();
    return photoPath+str(row[0])+'/'+str(row[1])+'.jpg';

def display_image():
    nextImage = get_image()
    if os.path.isfile(nextImage) :
        send_image_to_hdmi(nextImage)
        time.sleep(imageDuration)
    else:
        display_image()

try:
    while True:
        display_image()
except KeyboardInterrupt:
    print('Finished!')

