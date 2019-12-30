#Importation des bibliothèques nécessaires
from config.pyG_element import PyGame
import config.settings as const
from models.map import Map
from pygame.locals import *
import time


class Game:
    '''Represent the game'''
    
    def __init__(self):
        
        #Initialisation de la bibliothèque Pygame
        self.py = PyGame()
        self.clock = self.py.clock
        
        self.init()        
    
    def init(self):
        #Create and display map
        self.map = Map(self) 
        
        self.map.display_map()
        
        self.map.add_sprites()  
        
        self.win = False
        self.loose = False    
        
        self.start()  
    
    def start(self):
        #Variable qui continue la boucle si = 1, stoppe si = 0
        play = 1

        #Boucle infinie
        while play:
            self.clock.tick(30)
                        
            moved = False
            for event in self.py.event.get():
                if event.type == QUIT:
                    play = 0
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:	#Si "flèche bas"
                        moved = self.map.hero.move("down")
                    elif event.key == K_UP:	#Si "flèche bas"
                        moved = self.map.hero.move("up")
                    elif event.key == K_LEFT:	#Si "flèche bas"
                        moved = self.map.hero.move("left")
                    elif event.key == K_RIGHT:	#Si "flèche bas"
                        moved = self.map.hero.move("right")

                    if moved:
                        play = self.map.moved_actions()
            
            self.map.sprites.update()
            
            self.map.sprites.draw(self.py.screen)        
            
            #Rafraîchissement de l'écran
            self.py.display.flip()
                
        if self.win:
            self.win_game()
        elif self.loose:
            self.loose_game()
                
    def win_game(self):
        self.py.music.stop()            
        self.py.win_sound.play() 
        	
        time.sleep(.100)
        
        continu = self.continue_game()   
        if continu == 1:     
            self.init()
            #restart
        
    def loose_game(self):
        self.py.music.stop()            
        self.py.loose_sound.play()
        
        time.sleep(.100)
        
        continu = self.continue_game() 
        if continu == 1:     
            self.init()
            #restart
            
    def continue_game(self):
        text = self.py.font.render("Do you want to continue ? yes=y/no=n", True,  (255, 0, 0), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = self.py.screen.get_rect().centerx
        textrect.centery = self.py.screen.get_rect().centery 
        
        #Rafraîchissement de l'écran
        self.py.screen.blit(text, textrect)
        
        time.sleep(.200)
        
        continu = 0
        wait = True
        player_answer = False
        while wait:
            self.clock.tick(50) 
            for event in self.py.event.get():
                if event.type == QUIT:
                    continu = 0
                    wait = False
                elif event.type == KEYDOWN:
                    if event.key == K_y:	#Si "y"
                        continu = 1
                        wait = False              
                    elif event.key == K_n:	#Si "n"
                        continu = 0
                        wait = False
                        
            self.py.display.flip()
        
        return continu