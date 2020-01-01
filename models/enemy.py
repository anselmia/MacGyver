''' Import needed in the module '''
import random
import pygame as py
import config.settings as const
from config.pyg_element import PyGame
from .path import PathSprite
from .position import Position


class Enemy:
    ''' create instance of enemy, creating instance of EnemySprite and PathSprite
        PathSprite is used to replace enemy image after instance moved
        arg : board, spritesheet of enemies, position and enemy count '''

    def __init__(self, board, enemies_image, position, enemy_number):
        self.board = board
        self.position = position
        self.last_position = position

        enemy_image = PyGame.get_image_from_spritesheet(enemies_image,
                                                        enemy_number * const.SIZE_OF_SPRITE,
                                                        const.SIZE_OF_SPRITE)

        self.sprite = EnemySprite(enemy_image,
                                  self.position)

        self.path_sprite = PathSprite(board.py.images["path"],
                                      Position.get_random_free_position(board))

    def move(self):
        ''' Move the enemy position to it's next random possible position
        Try not return in the last position if possible'''

        try:
            around_paths = Position.next_possible_positions(self.board, self.position)

            if len(around_paths) > 1 and self.last_position in around_paths:
                around_paths.remove(self.last_position)

            new_position = random.sample(around_paths, 1)[0]
            self.path_sprite.next_position = self.position
            self.last_position = self.position
            self.position = new_position
            self.sprite.next_position = new_position

        except Exception as _e:
            print(_e)


class EnemySprite(py.sprite.Sprite):
    ''' Represent the enemy as a sprite
    Instantiate by image and initial position'''
    def __init__(self, enemy_image, init_position):
        super().__init__()

        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (init_position.position[1] * const.SIZE_OF_SPRITE,
                             init_position.position[0] * const.SIZE_OF_SPRITE)
        self.next_position = Position(self.rect.topleft[1] / const.SIZE_OF_SPRITE,
                                      self.rect.topleft[0] / const.SIZE_OF_SPRITE)
        self.order = None

    def update(self):
        ''' Method to update the instance position to the next position '''
        self.rect.topleft = (self.next_position.position[1] * const.SIZE_OF_SPRITE,
                             self.next_position.position[0] * const.SIZE_OF_SPRITE)
