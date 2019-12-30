import pygame as py
import config.settings as const


class TileSprite(py.sprite.Sprite):
    
    def __init__(self, tile_image, init_position, item_number):
        super().__init__()
        
        self.image = tile_image
        self.rect = self.image.get_rect()
        self.rect.topleft = init_position.position[1] * const.SIZE_OF_SPRITE, init_position.position[0] * const.SIZE_OF_SPRITE
        self.order = None
            
    def update(self):
        pass