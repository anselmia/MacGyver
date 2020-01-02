'''Module which contain all the pygame elements'''
import pygame as py
import pygame.locals as py_cst
import config.settings as const
from models.position import Position


class PyGame():
    ''' Class that will instantiate the pygame element needed in the project '''

    def __init__(self):
        py.init()

        self.screen = None
        self.images = []
        self.clock = py.time.Clock()
        self.event = py.event
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

        #Initialize a font for the displayed message
        self.font = py.font.SysFont("comicsansms", 20)

    def create_screen(self, map_size):
        ''' Create the game window with map arg size as window size arg '''

        self.screen = py.display.set_mode((map_size[1] * const.SIZE_OF_SPRITE,
                                           map_size[0] * const.SIZE_OF_SPRITE),
                                          py_cst.RESIZABLE)

    def load_image(self):
        ''' Load images to be used to display game '''

        self.images = {
            "wall": py.image.load(const.WALL_IMAGE).convert(),
            "guardian": py.image.load(const.GUARDIAN_IMAGE).convert_alpha(),
            "path": py.image.load(const.FOND_IMAGE).convert(),
            "hero": py.image.load(const.HERO_IMAGE).convert_alpha(),
            "tiles": py.image.load(const.TILES_IMAGE).convert_alpha(),
            "enemies": py.image.load(const.ENEMIES_IMAGE).convert_alpha()
            }

    def update_sprite(self, sprite_group):
        ''' Update the sprite position on window and refresh the window.
        Receive a sprite.group() as arg'''

        #Update all sprite position
        sprite_group.update()

        self.draw(sprite_group)

        self.refresh()

    def display_text(self, text):
        ''' Display text received as arg on window '''

        text = self.font.render(text,
                                   True, (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect() #Get the rect represented by the text area to be displayed
        textrect.centerx = self.screen.get_rect().centerx
        textrect.centery = self.screen.get_rect().centery

        #display the text on window
        self.blit(text, textrect)

    def display_map(self, map_size, paths):
        """ display walls and pathes
        arg : Map_size (x and y), paths positions"""

        for i in range(map_size[0] + 1):
            for j in range(map_size[1] + 1):
                if Position(i, j) not in paths:
                    self.blit(self.images["wall"],
                              (j * const.SIZE_OF_SPRITE, i * const.SIZE_OF_SPRITE))
                else:
                    self.blit(self.images["path"],
                              (j * const.SIZE_OF_SPRITE, i * const.SIZE_OF_SPRITE))

    def blit(self, image, rect):
        ''' Print an image on the window base on its rect arg '''
        self.screen.blit(image, rect)

    def refresh(self):
        ''' refresh the displayed window '''
        py.display.flip()

    def draw(self, sprite_group):
        ''' #redraw the sprites on the screen at the updated position.
        Receive a sprite.group() '''
        sprite_group.draw(self.screen)

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
