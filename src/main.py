# Example file showing a basic pygame "game loop"
import pygame as pg
import sys
from constants import FPS
from game import Game

# pygame setup
pg.init()
running: bool = True
clock = pg.time.Clock()
game: Game = Game()

game.create_display()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        #checking for user input
        game.map_cotrols()

        #checking if game over
        running = game.game_over()
        # add something to controls to check if r was hit after game over to start again
        # or if the restart button in the corner was hit
        


    clock.tick(FPS)  # limits FPS to 60

pg.quit()
sys.exit()