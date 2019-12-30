import config.settings as const
from .position import Position
from views.enemy import EnemySprite
from views.guardian import GuardianSprite
from views.tile import TileSprite
from views.map import MapSprite
from views.hero import HeroSprite
from .tile import Tile
from .enemy import Enemy
from .hero import Hero
from .sprite_group import SpriteGroup
import random


class Map:  

    def __init__(self, game):
        self.game = game
        self.filename = const.MAP_PATH
        self.py = game.py
        
        self._paths = set()
        self._start = set()
        self._end = set()
        self._tiles_position = set()   
        self._enemies_position = set() 
        
        self.tiles = []
        self.enemies = []
        self._available_tiles = const.NUMBER_OF_TILES
        
        self.map_size = self.load_from_file()  
        
        #Create game window
        self.py.create_screen(self.map_size)
        self.py.load_image()
        
        self.sprites = None 

    def __contains__(self, position):
        return position in self._paths

    @property
    def start(self):
        return list(self._start)[0]
    
    @property
    def end(self):
        return list(self._end)[0]
    
    @property
    def paths(self):
        return self._paths
    
    def load_from_file(self):
        len_x = 0
        len_y = 0
        
        with open(self.filename) as infile:            
            for x, line in enumerate(infile):
                len_x += 1
                len_y = len(line)
                for y, c in enumerate(line):
                    if c == const.PATH_CHAR:
                        self._paths.add(Position(x,y))
                    elif c == const.START_CHAR:
                        self._paths.add(Position(x,y))
                        self._start.add(Position(x,y))
                    elif c == const.END_CHAR:
                        self._paths.add(Position(x,y))
                        self._end.add(Position(x,y))
        
        return len_x, len_y
    
    def add_sprites(self):
        self.sprites = SpriteGroup()
        
        self.add_guardian()
        self.add_tiles()     
        self.add_enemies()   
        self.add_hero()   
        
        x = 0
        for sprite in [sprite for sprite in self.sprites if isinstance(sprite, MapSprite)]:
            sprite.order = x
            x += 1
            
        for sprite in [sprite for sprite in self.sprites if isinstance(sprite, TileSprite)]:
            sprite.order = x
            x += 1
            
        for sprite in [sprite for sprite in self.sprites if isinstance(sprite, GuardianSprite)]:
            sprite.order = x
            x += 1
            
        for sprite in [sprite for sprite in self.sprites if isinstance(sprite, EnemySprite)]:
            sprite.order = x
            x += 1
            
        for sprite in [sprite for sprite in self.sprites if isinstance(sprite, HeroSprite)]:
            sprite.order = x
            x += 1
    
    def add_hero(self):
        self.hero = Hero(self)
        self.sprites.add(self.hero.sprite)
        self.sprites.add(self.hero.map_sprite)
    
    def add_guardian(self):
        self.guardian_sprite = GuardianSprite(self.py.guardian, self.end)
        self.sprites.add(self.guardian_sprite)
    
    def add_tiles(self): 
        for x in range(const.NUMBER_OF_TILES):
            free_path = self.get_random_free_path()
            self._tiles_position.add(free_path)
            tile = Tile(self.py.tiles, free_path, x)
            self.tiles.append(tile)
            self.sprites.add(tile.sprite)
            
    def add_enemies(self): 
        for x in range(const.NUMBER_OF_ENEMIES):
            free_path = self.get_random_free_path()
            self._enemies_position.add(free_path)
            enemy = Enemy(self, self.py.enemies, free_path, x)
            self.enemies.append(enemy)
            self.sprites.add(enemy.sprite)            
            self.sprites.add(enemy.map_sprite)
    
    def get_random_free_path(self):
        '''Get a random path remaining in the free path after removing object path on map'''
        free_path = self._paths.copy() - self._start - self._end - self._tiles_position - self._enemies_position
        return random.sample(free_path, 1)[0]
    
    def get_free_paths(self):
        '''Get all path remaining in the free path after removing object path on map'''
        free_paths = self._paths - self._start - self._end - self._tiles_position - self._enemies_position
        return free_paths
    
    def get_free_paths_around(self, position):
        next_posible_paths = set()
        free_paths = self.get_free_paths()
        
        around_positions = set()
        around_positions.add(getattr(position, "right")())
        around_positions.add(getattr(position, "left")())
        around_positions.add(getattr(position, "up")())
        around_positions.add(getattr(position, "down")())
        
        for position in around_positions:
            if position in free_paths:
                next_posible_paths.add(position)
    
        return next_posible_paths
                
    def moved_actions(self):
        self.check_tile_path()
        self.move_enemies()
        
        play, self.game.loose = self.hero.check_colision([sprite for sprite in self.sprites if isinstance(sprite, EnemySprite)])
        
        if self.hero.position == self.end:
            self.check_win()
            play = 0
        
        return play
                
    def check_tile_path(self):
        Tile = None
        for tile in self.tiles:
            if self.hero.position == tile.position:
                self.py.item_sound.play()
                self._available_tiles -=1
                tile.collected = True
                self.sprites.remove(tile.sprite)
                Tile = tile
                break
        
        if Tile != None:
            self.tiles.remove(Tile)
    
    def check_win(self):
        if self._available_tiles == 0:
            self.game.win = True
        else:            
            self.game.loose = True
    
    def display_map(self):
        """Reads the level table, displays walls and path"""       
        
        for i in range(self.map_size[0] + 1):
            for j in range(self.map_size[1] + 1):
                if Position(i,j) not in self._paths:
                    self.py.screen.blit(self.py.wall, (j * const.SIZE_OF_SPRITE, i * const.SIZE_OF_SPRITE))
                else:
                    self.py.screen.blit(self.py.fond, (j * const.SIZE_OF_SPRITE, i * const.SIZE_OF_SPRITE))

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()
    
def main():
    map = Map('data/maps/map.txt')
    p = Position(-1, 0)
    print(p in map)
    
if __name__ == "__main__":
    main()