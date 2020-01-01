''' Import needed in the module '''
import pygame as py
import config.settings as const
from config.pyg_element import PyGame


class Tile:
    ''' create instance of tile, creating instance of TileSprite
        arg : spritesheet of Tiles, position and tile count'''

    def __init__(self, tiles_image, position, item_number):
        self.position = position
        self.collected = False
        self.sprite = TileSprite(PyGame.get_image_from_spritesheet(
            tiles_image,
            item_number * const.SIZE_OF_SPRITE,
            const.SIZE_OF_SPRITE),
                                 self.position)


class TileSprite(py.sprite.Sprite):
    ''' instance of TileSprite representing a tile as a sprite '''

    def __init__(self, tile_image, init_position):
        super().__init__()

        self.image = tile_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (init_position.position[1] * const.SIZE_OF_SPRITE,
                             init_position.position[0] * const.SIZE_OF_SPRITE)
        self.order = None
