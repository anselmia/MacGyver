''' Import needed in the module '''
import pygame as py
import config.settings as const
from .path import PathSprite
from .position import Position
from .enemy import EnemySprite

class Hero:
    ''' instance of hero, creating instance of EnemySprite and PathSprite
        arg : board, spritesheet of enemies, position and enemy count'''

    def __init__(self, board):
        self.board = board
        self.position = next(iter(board.start))
        self.last_position = self.position

        self.sprite = HeroSprite(board.py.images["hero"], self.position)

        self.path_sprite = PathSprite(board.py.images["path"],
                                      Position.get_random_free_position(board))

    def move(self, direction):
        ''' Take (str) direction as arg and try to move instance position according to arg
        if move is possible, update accordingly members position
        return True if move is possible, false if not '''

        #getattr can access an object property using a string
        new_position = getattr(self.position, direction)()

        if new_position in self.board:
            self.path_sprite.next_position = self.position
            self.last_position = self.position
            self.position = new_position
            self.sprite.next_position = new_position
            return True

        return False

    def check_colision(self):
        ''' Take enemies sprite as arg and compare their position with instance position
        return 0 if no matches, 1 if positive matche'''

        enemies = [sprite for sprite in self.board.sprites if isinstance(sprite, EnemySprite)]
        for sprite in enemies:
            sprite_pos = Position(sprite.rect.top / const.SIZE_OF_SPRITE,
                                  sprite.rect.left / const.SIZE_OF_SPRITE)
            if sprite_pos in (self.position, self.last_position):
                return 0, True

        return 1, False


class HeroSprite(py.sprite.Sprite):
    ''' Represent the hero as a sprite
    Instantiate by image and initial position'''

    def __init__(self, hero_image, pos):
        super().__init__()
        self.image = hero_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos.position[1] * const.SIZE_OF_SPRITE,
                             pos.position[0] * const.SIZE_OF_SPRITE)
        self.next_position = Position(self.rect.topleft[0], self.rect.topleft[1])
        self.order = None

    def update(self):
        ''' Method to update the instance position to the next position '''
        self.rect.topleft = (self.next_position.position[1] * const.SIZE_OF_SPRITE,
                             self.next_position.position[0] * const.SIZE_OF_SPRITE)
