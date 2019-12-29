import pygame as py
import config.settings as const
from models.position import Position


class MapSprite(py.sprite.Sprite):
    
    def __init__(self, init_position):
        super().__init__()
        self.image = py.image.load(const.FOND_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = init_position[0].position[1], init_position[0].position[0]
        self.next_position = Position(self.rect.topleft[0], self.rect.topleft[1])
       
    def update(self):
        self.rect.topleft = self.next_position.position[1] * const.SIZE_OF_SPRITE, self.next_position.position[0] * const.SIZE_OF_SPRITE