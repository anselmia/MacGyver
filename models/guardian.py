''' Import needed in the module '''
import pygame as py
import config.settings as const


class GuardianSprite(py.sprite.Sprite):
    ''' Represent the Guardian as a sprite
    Instantiate by image and initial position'''

    def __init__(self, guardian_image, init_position):
        super().__init__()
        self.image = guardian_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (init_position.position[1] * const.SIZE_OF_SPRITE,
                             init_position.position[0] * const.SIZE_OF_SPRITE)
        self.order = None
