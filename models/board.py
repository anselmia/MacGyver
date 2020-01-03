''' Import needed in the module '''
import config.settings as const
from .enemy import EnemySprite
from .hero import HeroSprite
from .guardian import GuardianSprite
from .position import Position
from .path import PathSprite
from .tile import TileSprite
from .sprite_group import SpriteGroup

class Board:
    ''' Instance of the game map.
    Contains all the sprites'''

    def __init__(self, game):
        self.game = game
        self.py = game.py

        self._positions = {
            "paths":[],
            "start": None,
            "end": None
        }

        self.map_size = self.load_from_file()

        self.hero = None
        self.sprites = None

    def __contains__(self, position):
        return position in self._positions["paths"]

    @property
    def start(self):
        ''' Game start position '''
        return self._positions["start"]

    @property
    def end(self):
        ''' Game end position '''
        return self._positions["end"]

    @property
    def paths(self):
        ''' Paths position '''
        return self._positions["paths"]

    @property
    def tiles_position(self):
        ''' Tiles position '''
        tiles = [sprite for sprite in self.sprites if isinstance(sprite, TileSprite)]
        return [tile.position for tile in tiles]

    @property
    def enemies_position(self):
        ''' Enemies position '''
        enemies = [sprite for sprite in self.sprites if isinstance(sprite, EnemySprite)]

        return [enemy.pos["actual"] for enemy in enemies]

    def load_from_file(self):
        ''' From a txt file, read lines and characters
        and convert it to map positions. '''

        len_x = 0
        len_y = 0

        with open(const.MAP_PATH) as infile:
            for x, line in enumerate(infile):
                len_x += 1
                len_y = len(line)
                for y, c in enumerate(line):
                    if c == const.PATH_CHAR:
                        self._positions["paths"].append(Position(x, y))
                    elif c == const.START_CHAR:
                        self._positions["paths"].append(Position(x, y))
                        self._positions["start"] = Position(x, y)
                    elif c == const.END_CHAR:
                        self._positions["paths"].append(Position(x, y))
                        self._positions["end"] = Position(x, y)

        return len_x, len_y

    def add_sprites(self):
        ''' Add all characters to board by creating new instance.
        Add all sprites instances created by character to a group of sprite
        calculate sprite order and set corresponding sprite instance with the corresponding order
        Order is used to draw sprites '''

        self.sprites = SpriteGroup()

        self.add_guardian()
        self.add_tiles()
        self.add_enemies()
        self.add_hero()

        x = 0
        for sprite in [sprite for sprite in self.sprites if isinstance(sprite, PathSprite)]:
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
        ''' Create instance of hero
        Add hero and map sprite from hero instance to the sprites group'''

        self.hero = HeroSprite(self, self.py.images["hero"])
        self.sprites.add(self.hero)
        self.sprites.add(self.hero.path_sprite)

    def add_guardian(self):
        ''' Create instance of guardian sprite and
        add it to the sprites group'''

        guardian_sprite = GuardianSprite(self.py.images["guardian"], self.end)
        self.sprites.add(guardian_sprite)

    def add_tiles(self):
        ''' Create instances of tiles
        Add tiles sprite from tiles instance to the sprites group'''

        for x in range(const.NUMBER_OF_TILES):
            free_position = Position.get_random_free_position(self)
            tile = TileSprite(self.py.images["tiles"], free_position, x)
            self.sprites.add(tile)

    def add_enemies(self):
        ''' Create instances of enemies
        Add enemies and maps sprite from enemies instance to the sprites group '''

        for x in range(const.NUMBER_OF_ENEMIES):
            free_position = Position.get_random_free_position(self)
            enemy = EnemySprite(self, free_position, x)
            self.sprites.add(enemy)
            self.sprites.add(enemy.path_sprite)

    def check_tile_path(self):
        ''' Get tiles positions and compare to hero position
        if position is eq, play a sound, set the tile eq to
        hero position as "collected" and remove the tile from board'''

        tiles = [sprite for sprite in self.sprites if isinstance(sprite, TileSprite)]
        for tile in tiles:
            if self.hero.pos["actual"] == tile.position:
                self.py.sounds["item_sound"].play()
                tile.collected = True
                self.sprites.remove(tile)
                break

    def check_win(self):
        ''' Verify win condition '''

        tiles = [sprite for sprite in self.sprites if isinstance(sprite, TileSprite)]
        for tile in tiles:
            if tile.collected is False:
                self.game.loose = True
                break

        if self.game.loose is False:
            self.game.win = True

    def move_enemies(self):
        """ update enemies positions """
        enemies = [sprite for sprite in self.sprites if isinstance(sprite, EnemySprite)]
        for _enemy in enemies:
            _enemy.move()
