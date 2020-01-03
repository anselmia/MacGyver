''' Import needed in the module '''
import pygame as py
import config.settings as const
from config.pyg_element import PyGame


class TileSprite(py.sprite.Sprite):
    ''' instance of TileSprite representing a tile as a sprite '''

    def __init__(self, tiles_images, init_position, item_number):
        super().__init__()

        self.image = PyGame.get_image_from_spritesheet(
            tiles_images,
            item_number * const.SIZE_OF_SPRITE)
        self.position = init_position
        self.rect = self.image.get_rect()
        self.rect.topleft = (init_position.position[1] * const.SIZE_OF_SPRITE,
                             init_position.position[0] * const.SIZE_OF_SPRITE)
        self.collected = False        
        self.order = None
