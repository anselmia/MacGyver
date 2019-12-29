from pygame.locals import *

class Game_Event():
    
    @staticmethod
    def get_event(pygame, hero):
        moved = False
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:	#Si "flèche bas"
                    moved = hero.move("down")
                elif event.key == K_UP:	#Si "flèche bas"
                    moved =hero.move("up")
                elif event.key == K_LEFT:	#Si "flèche bas"
                    moved =hero.move("left")
                elif event.key == K_RIGHT:	#Si "flèche bas"
                    moved =hero.move("right")
                    
                if moved:
                    hero.map.check_tile_path()
                    if hero.position == hero.map.end:
                        hero.map.check_win()
                        return 0

        return 1