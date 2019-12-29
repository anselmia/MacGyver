import pygame as py
import config.settings as const


class TileSprite(py.sprite.Sprite):
    
    def __init__(self, init_position, item_number):
        super().__init__()
        self.sprite_sheet = py.image.load(const.TILES_IMAGE).convert()
        
        self.image = self.get_image(item_number * const.SIZE_OF_SPRITE, const.SIZE_OF_SPRITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = init_position.position[1] * const.SIZE_OF_SPRITE, init_position.position[0] * const.SIZE_OF_SPRITE
        
    def get_image(self, x, sprite_size):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = py.Surface([sprite_size, sprite_size]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, 0, sprite_size, sprite_size))
 
        # Assuming black works as the transparent color
        image.set_colorkey((0,0,0))
 
        # Return the image
        return image
    
    def update(self):
        pass