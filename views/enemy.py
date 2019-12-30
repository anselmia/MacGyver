import pygame as py
import config.settings as const
from models.position import Position


class EnemySprite(py.sprite.Sprite):
    
    def __init__(self, enemy_image, init_position, enemy_number):
        super().__init__()
        
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.topleft = init_position.position[1] * const.SIZE_OF_SPRITE, init_position.position[0] * const.SIZE_OF_SPRITE
        self.next_position = Position(self.rect.topleft[1] / const.SIZE_OF_SPRITE, self.rect.topleft[0] / const.SIZE_OF_SPRITE)
        self.order = None
    
    def update(self):
        self.rect.topleft = self.next_position.position[1] * const.SIZE_OF_SPRITE, self.next_position.position[0] * const.SIZE_OF_SPRITE  