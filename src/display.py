from decimal import *
import pygame

class Display:
    max_width: None
    max_height: None
    canvas: None

    def __init__(self, width, height):
        self.max_width = width
        self.max_height = height

    def send_to_hdmi(self, imageData):
        image = self.load_image(imageData['path'])
        image = self.resize_image(image);
        self.render_image(image)

        pygame.mouse.set_visible(0)
        pygame.display.update()

    def load_image(self, imagePath):
        try:
            return pygame.image.load(imagePath)
        except:
            print( "Bad image")
            print( imagePath )
            quit()

    def resize_image(self, image):
        size = image.get_rect()
        width = size[2]
        height = size[3]
        if width > self.max_width:
             height = height * (Decimal(self.max_width)/Decimal(width))
             width = self.max_width
             image = pygame.transform.scale(image,(width,height))
        if height > self.max_height:
             width = width * (Decimal(self.max_height)/Decimal(height))
             height = self.max_height
             image = pygame.transform.scale(image,(width,height))
        return image

    def render_image(self, image):
        self.canvas = pygame.display.set_mode((self.max_width,self.max_height),pygame.FULLSCREEN)
        self.canvas.blit(image,(0,0))

    # def render_caption():
    #     # todo

