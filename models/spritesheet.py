import pygame as py


class SpriteSheet():
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
 
        # Load the sprite sheet.
        self.sprite_sheet = py.image.load(file_name).convert()
 
 
    