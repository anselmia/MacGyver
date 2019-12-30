from events.events import Event
from views.tile import TileSprite
import config.settings as const
from config.pyG_element import PyGame


class Tile:
    
    def __init__(self,tiles_image, position, item_number):
        self.position = position
        self.collected = False
        self.item_number = item_number
        self.sprite = TileSprite(PyGame.get_image_from_spritesheet(tiles_image, item_number * const.SIZE_OF_SPRITE, const.SIZE_OF_SPRITE),
                                self.position,
                                item_number)       


def main():
    pass

if __name__ == "__main__":
    main()