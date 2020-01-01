'''Module which contain all the pygame elements'''
import pygame as py
import pygame.locals as py_cst
import config.settings as const


class PyGame():
    ''' Class that will instantiate the pygame element needed in the project '''

    def __init__(self):
        py.init()

        self.screen = None
        self.images = []
        self.clock = py.time.Clock()
        self.event = py.event
        self.group = py.sprite.Group()
        self.display = py.display
        self.const = py_cst

        #Load game music
        py.mixer.music.load(const.MUSIC)

        #Load sound to be played during game on certain event
        self.sounds = {
            "game_music": py.mixer.music,
            "item_sound": py.mixer.Sound(const.SOUND_ITEM),
            "win_sound": py.mixer.Sound(const.SOUND_WIN),
            "loose_sound": py.mixer.Sound(const.SOUND_LOOSE)
            }

        #Play game music in infinite loop
        #self.sounds["game_music"].play(-1)

        #Initialize a font for the displayed message
        self.font = py.font.SysFont("comicsansms", 20)

    def create_screen(self, map_size):
        ''' Create the game window with map arg size as window size arg '''

        self.screen = py.display.set_mode((map_size[1] * const.SIZE_OF_SPRITE,
                                           map_size[0] * const.SIZE_OF_SPRITE),
                                           py_cst.RESIZABLE)

    def load_image(self):
        ''' Load images to be used to construct game '''

        self.images = {
            "wall": py.image.load(const.WALL_IMAGE).convert(),
            "guardian": py.image.load(const.GUARDIAN_IMAGE).convert_alpha(),
            "path": py.image.load(const.FOND_IMAGE).convert(),
            "hero": py.image.load(const.HERO_IMAGE).convert_alpha(),
            "tiles": py.image.load(const.TILES_IMAGE).convert_alpha(),
            "enemies": py.image.load(const.ENEMIES_IMAGE).convert_alpha()
            }

    @staticmethod
    def get_image_from_spritesheet(tiles_image, x, sprite_size):
        """ Grab a single image out of a larger spritesheet
        Pass in the x location of the sprite
        and the size of the sprite. """

        # Create a new blank image
        image = py.Surface([sprite_size, sprite_size]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(tiles_image, (0, 0), (x, 0, sprite_size, sprite_size))

        # Assuming black works as the transparent color
        image.set_colorkey((0, 0, 0))

        # Return the image
        return image
