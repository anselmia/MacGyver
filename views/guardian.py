import pygame as py
import config.settings as const


class GuardianSprite(py.sprite.Sprite):
    
    def __init__(self, init_position):
        super().__init__()
        self.image = py.image.load(const.GUARDIAN_IMAGE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = init_position.position[1] * const.SIZE_OF_SPRITE, init_position.position[0] * const.SIZE_OF_SPRITE
        
    def update(self):
        pass