from views.hero import HeroSprite
from views.map import MapSprite

class Hero:

    def __init__(self, map):
        self.map = map
        self.position = self.map.start
        self.sprite = HeroSprite(map.py.hero) 
        self.map_sprite = MapSprite(self.map.py.fond, self.map.get_random_free_path())       
   
    def move(self, direction):
        
        #getattr can access an object property using a sing 
        new_position = getattr(self.position, direction)()
        
        if new_position in self.map:
            self.map_sprite.next_position = self.position
            self.position = new_position        
            self.sprite.next_position = new_position
            return True
        
        return False
            
def main():
    pass

if __name__ == "__main__":
    main()