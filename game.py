#Importation des bibliothèques nécessaires
from config.pyG_element import PyGame
import config.settings as const
from events.game_event import Game_Event
from models.hero import Hero
from models.map import Map
from controllers.keyboard import KeyboardController


class Game:
    '''Represent the game'''
    
    def __init__(self):
        
        #Initialisation de la bibliothèque Pygame
        self.py = PyGame()
        
        #Create and display map
        self.map = Map(self.py)
        
        self.keyboard = KeyboardController()
                   
        self.hero = Hero(self.map)
        
        self.map.display_map()
        
        self.map.add_sprites(self.hero)        
        
        self.clock = self.py.clock
        
    def start(self):
        #Variable qui continue la boucle si = 1, stoppe si = 0
        continuer = 1

        #Boucle infinie
        while continuer:
            self.clock.tick(30)
            
            continuer = Game_Event.get_event(self.py.event, self.hero)
            
            self.map.sprites.update()
            
            updated_sprites = self.map.sprites.draw(self.py.screen)        
            
            #Rafraîchissement de l'écran
            self.py.display.flip()