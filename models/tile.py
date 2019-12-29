from events.events import Event
from views.tile import TileSprite
import config.settings as const


class Tile:
    
    def __init__(self, position, item_number):
        self.position = position
        self.collected = False
        self.item_number = item_number
        self.sprite = TileSprite(self.position, item_number)        
    
        
    
def main():
    pass

if __name__ == "__main__":
    main()