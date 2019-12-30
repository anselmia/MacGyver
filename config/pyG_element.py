import pygame as py
from pygame.locals import *
import config.settings as const


class PyGame():
    
    def __init__(self):
        py.init()
        
        self.clock = py.time.Clock()
        self.event = py.event
        self.group = py.sprite.Group()
        self.display = py.display
        
        self.map = None
        
        #Load music and play it in infinite loop
        py.mixer.music.load(const.MUSIC)
        self.music = py.mixer.music
        #self.music.play(-1)
        
        #Load sound to be played during game on certain event
        self.item_sound = py.mixer.Sound(const.SOUND_ITEM)
        self.win_sound = py.mixer.Sound(const.SOUND_WIN)
        self.loose_sound = py.mixer.Sound(const.SOUND_LOOSE)
        
        #Initialize a font for the displayed message    
        self.font = py.font.SysFont("comicsansms", 20)
        
    def create_screen(self, map_size):
        '''Create the game window with map arg size as window size arg'''
        self.screen = py.display.set_mode((map_size[1] * const.SIZE_OF_SPRITE, map_size[0] * const.SIZE_OF_SPRITE) , RESIZABLE)
        
    def load_image(self):
         #Load images to be used to construct game
        self.wall = py.image.load(const.WALL_IMAGE).convert()
        self.guardian = py.image.load(const.GUARDIAN_IMAGE).convert_alpha()
        self.fond = py.image.load(const.FOND_IMAGE).convert()
        self.hero = py.image.load(const.HERO_IMAGE).convert_alpha()
        self.tiles = py.image.load(const.TILES_IMAGE).convert_alpha()
        self.enemies = py.image.load(const.ENEMIES_IMAGE).convert_alpha()
    
    @staticmethod
    def get_image_from_spritesheet(tiles_image, x, sprite_size):
        """ Grab a single image out of a larger spritesheet
        Pass in the x, y location of the sprite
        and the size of the sprite. """
 
        # Create a new blank image
        image = py.Surface([sprite_size, sprite_size]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(tiles_image, (0, 0), (x, 0, sprite_size, sprite_size))
 
        # Assuming black works as the transparent color
        image.set_colorkey((0,0,0))
 
        # Return the image
        return image