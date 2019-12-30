from config.pyG_element import PyGame
from views.enemy import EnemySprite
from views.map import MapSprite
from .position import Position
import config.settings as const
import random


class Enemy:
    
    def __init__(self, map, enemies_image, position, item_number):
        self.map = map
        self.position = position
        self.collected = False
        self.item_number = item_number
        self.sprite = EnemySprite(PyGame.get_image_from_spritesheet(enemies_image, item_number * const.SIZE_OF_SPRITE, const.SIZE_OF_SPRITE),
                                  self.position,
                                  item_number)     
        self.map_sprite = MapSprite(self.map.py.fond, self.map.get_random_free_path())       
    
    def move(self):
        try:
            around_paths = self.map.get_free_paths_around(Position(self.sprite.rect.top / const.SIZE_OF_SPRITE,
                                                                   self.sprite.rect.left / const.SIZE_OF_SPRITE))
            new_position = random.sample(around_paths, 1)[0]
            self.map_sprite.next_position = self.position
            self.position = new_position
            self.sprite.next_position = new_position
        
        except:
            pass
          
          
def main():
    pass

if __name__ == "__main__":
    main()