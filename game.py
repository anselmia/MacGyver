''' Module to import to run the game '''
import time
from config.pyg_element import PyGame
import config.settings as const
from models.board import Board


class Game:
    ''' Running the game and gestion of game '''

    def __init__(self):

        #Initialisation of pygame module and declaration of
        #the variable to be used in the application        
        self.py = PyGame()
        self.clock = self.py.clock

        #Game initialization (used to restart the game)
        self.init()

    def init(self):
        ''' Initialisation of game '''

        #Create and display map
        self.board = Board(self)

        #Create game window
        self.py.create_screen(self.board.map_size)

        #Load Images for building the interface and characters
        self.py.load_image()

        #Print the map on screen
        self.py.display_map(self.board.map_size,  self.board.paths)

        #Add characters to the board
        self.board.add_sprites()

        #Play game music in infinite loop
        self.py.sounds["game_music"].play(-1)

        self.win = False
        self.loose = False

        self.start()

    def start(self):
        ''' Execute the game's actions in a loop awaiting for player instructions '''

        #Condition to run the game
        play = 1

        while play:
            self.clock.tick(const.FPS) #Setting the game FPS

            moved = False
            for event in self.py.event.get():
                if event.type == self.py.const.QUIT:
                    play = 0
                elif event.type == self.py.const.KEYDOWN:
                    if event.key == self.py.const.K_DOWN:	#if down key"
                        moved = self.board.hero.move("down")
                    elif event.key == self.py.const.K_UP:	#if up key"
                        moved = self.board.hero.move("up")
                    elif event.key == self.py.const.K_LEFT:	#if lef key"
                        moved = self.board.hero.move("left")
                    elif event.key == self.py.const.K_RIGHT:	#if right key"
                        moved = self.board.hero.move("right")

                    if moved: #required actions when hero moved
                        self.board.check_tile_path()
                        self.board.move_enemies()

                        play, self.loose = self.board.hero.check_colision()

                        if self.board.hero.pos["actual"] == self.board.end:
                            self.board.check_win()
                            play = 0

            self.py.update_sprite(self.board.sprites)

        if self.win:
            self.win_game()
        elif self.loose:
            self.loose_game()

    def win_game(self):
        ''' Actions to be done when player win the game '''

        self.py.sounds["game_music"].stop()
        self.py.sounds["win_sound"].play()

        time.sleep(.100)

        continu = self.continue_game()
        if continu == 1:
            #restart the game
            self.init()

    def loose_game(self):
        ''' Actions to be done when player loose the game '''

        self.py.sounds["game_music"].stop()
        self.py.sounds["loose_sound"].play()

        time.sleep(.100)

        continu = self.continue_game()
        if continu == 1:
            #restart the game
            self.init()

    def continue_game(self):
        ''' Print a message to the player and await for the answer.
        Exit or restart the game '''

        #Display text on window
        self.py.display_text("Do you want to continue ? yes=y/no=n")

        time.sleep(.200)

        continu = 0
        wait = True
        while wait:
            self.clock.tick(50)
            for event in self.py.event.get():
                if event.type == self.py.const.QUIT:
                    wait = False
                elif event.type == self.py.const.KEYDOWN:
                    if event.key == self.py.const.K_y:	#if "y"
                        continu = 1
                        wait = False
                    elif event.key == self.py.const.K_n:	#if "n"
                        wait = False

            self.py.refresh()

        return continu
