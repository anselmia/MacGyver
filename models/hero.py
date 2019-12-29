from views.hero import HeroSprite


class Hero:

    def __init__(self, map, screen):
        self.map = map
        self.position = self.map.start
        self.screen = screen
        self.items_collected = 0
        self.sprite = HeroSprite()        
   
    def move(self, direction):
        
        #getattr can access an object property using a sing 
        new_position = getattr(self.position, direction)()
        
        if new_position in self.map:
            self.map.sprite.next_position = self.position
            self.position = new_position        
            self.sprite.next_position = new_position
            return True
        
        return False
            
def main():
    pass

if __name__ == "__main__":
    main()