#Importation des bibliothèques nécessaires
import pygame as py
from pygame.locals import *

import config.settings as const
from events.game_event import Game_Event
from models.hero import Hero
from models.map import Map
from controllers.keyboard import KeyboardController


class Game:
    '''Represent the game'''
    
    def __init__(self):
        
        #Initialisation de la bibliothèque Pygame
        py.init()
        
        #Create and display map
        self.map = Map()
        
        #Create game window
        self.screen = py.display.set_mode((self.map.map_size[1] * const.SIZE_OF_SPRITE, self.map.map_size[0] * const.SIZE_OF_SPRITE) , RESIZABLE)
        
        py.mixer.music.load(const.MUSIC)
        py.mixer.music.play(-1)

        self.keyboard = KeyboardController()
                   
        self.hero = Hero(self.map, (self.screen))
        self.map.display_map(self.screen)
        
        self.map.add_map_sprite()
        self.map.add_hero(self.hero)
        self.map.add_guardian()
        self.map.add_tiles()         
                        
        self.sprites = py.sprite.Group()
        self.sprites.add(self.hero.sprite)
        self.sprites.add(self.map.sprite)
        self.sprites.add(self.map.guardian_sprite)
        self.map.sprites = self.sprites
        
        for tile in self.map.tiles:
            self.sprites.add(tile.sprite)
        
        self.clock = py.time.Clock()
        
    def start(self):
        #Variable qui continue la boucle si = 1, stoppe si = 0
        continuer = 1

        #Boucle infinie
        while continuer:
            self.clock.tick(30)
            
            continuer = Game_Event.get_event(py, self.hero)
            
            self.sprites.update()
            
            updated_sprites = self.sprites.draw(self.screen)        
            
            #Rafraîchissement de l'écran
            py.display.flip()