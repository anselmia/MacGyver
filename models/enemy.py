''' Import needed in the module '''
import random
import pygame as py
import config.settings as const
from config.pyg_element import PyGame
from .path import PathSprite
from .position import Position


class EnemySprite(py.sprite.Sprite):
    ''' Represent the enemy as a sprite
    Instantiate by image and initial position'''
    def __init__(self, board, init_position, enemy_number):
        super().__init__()

        self.board = board
        self.image = PyGame.get_image_from_spritesheet(self.board.py.images["enemies"],
                                                       enemy_number * const.SIZE_OF_SPRITE)
        self.rect = self.image.get_rect()
        self.pos = {
            "actual": init_position,
            "last": init_position
        }
        self.path_sprite = PathSprite(self.board,
                                      Position.get_random_free_position(board))
        self.order = None

    def move(self):
        ''' Move the enemy position to it's next random possible position
        Try not return in the last position if possible'''

        around_paths = Position.next_possible_positions(self.board, self.pos["actual"])
        if len(around_paths) > 1 and self.pos["last"] in around_paths:
            around_paths.remove(self.pos["last"])
        new_position = random.choice(around_paths)
        self.pos["last"] = self.pos["actual"]
        self.path_sprite.position = self.pos["actual"]
        self.pos["actual"] = new_position

    def update(self):
        ''' Method to update the instance position to the next position '''
        self.rect.topleft = (self.pos["actual"].position[1] * const.SIZE_OF_SPRITE,
                             self.pos["actual"].position[0] * const.SIZE_OF_SPRITE)
