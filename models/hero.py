from views.hero import HeroSprite
from views.map import MapSprite
from views.enemy import EnemySprite
import config.settings as const
from .position import Position


class Hero:

    def __init__(self, map):
        self.map = map
        self.position = self.map.start
        self.last_position = self.position
        self.sprite = HeroSprite(map.py.hero) 
        self.map_sprite = MapSprite(self.map.py.fond, self.map.get_random_free_path())       
   
    def move(self, direction):
        
        #getattr can access an object property using a sing 
        new_position = getattr(self.position, direction)()
        
        if new_position in self.map:
            self.map_sprite.next_position = self.position
            self.last_position = self.position
            self.position = new_position        
            self.sprite.next_position = new_position
            return True
        
        return False
    
    def check_colision(self, enemies):
        for sprite in enemies:
            sprite_pos = Position(sprite.rect.top / const.SIZE_OF_SPRITE, sprite.rect.left / const.SIZE_OF_SPRITE)
            if sprite_pos == self.position or sprite_pos == self.last_position:
            #if sprite.rect.colliderect(self.hero.sprite.rect):
                return 0, True
    
        return 1, False
    
            
def main():
    pass

if __name__ == "__main__":
    main()