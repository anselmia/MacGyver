''' Import needed in the module '''
import pygame as py
import config.settings as const
from .path import PathSprite
from .position import Position
from .enemy import EnemySprite


class HeroSprite(py.sprite.Sprite):
    ''' Represent the hero as a sprite
    Instantiate by image and initial position'''

    def __init__(self, board, hero_image):
        super().__init__()
        self.image = hero_image
        self.rect = self.image.get_rect()

        self.board = board
        self.pos = {
            "actual": board.start,
            "last": None
            }
        self.path_sprite = PathSprite(self.board, Position.get_random_free_position(board))
        self.order = None

    def move(self, direction):
        ''' Take (str) direction as arg and try to move instance position according to arg
        if move is possible, update accordingly members position
        return True if move is possible, false if not '''

        #getattr can access an object property using a string
        new_position = getattr(self.pos["actual"], direction)()

        if new_position in self.board:
            self.path_sprite.position = self.pos["actual"]
            self.pos["last"] = self.pos["actual"]
            self.pos["actual"] = new_position
            return True

        return False

    def check_colision(self):
        ''' Take enemies sprite as arg and compare their position with instance position
        return 0 if no matches, 1 if positive matche'''

        enemies = [sprite for sprite in self.board.sprites if isinstance(sprite, EnemySprite)]
        for enemy in enemies:
            if (enemy.pos["actual"] == self.pos["actual"])\
                or (self.pos["actual"] == enemy.pos["last"]
                    and enemy.pos["actual"] == self.pos["last"]):
                return 0, True

        return 1, False

    def update(self):
        ''' Method to update the instance position to the next position '''
        self.rect.topleft = (self.pos["actual"].position[1] * const.SIZE_OF_SPRITE,
                             self.pos["actual"].position[0] * const.SIZE_OF_SPRITE)
