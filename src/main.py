import pygame as pg
import sys
from constants import FPS
from game import Game
import asyncio

pg.init()
running: bool = True
clock = pg.time.Clock()
game: Game = Game()

game.create_display()
is_game_over: bool = False

async def main():
    global running, is_game_over
    while running:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            #checking if user clicked to restart game or clicked the key
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if game.display.restart_button_rect.collidepoint(event.pos):
                        game.restart()
                    else: 
                        game.display.handle_key_click(event.pos)

            #checking for key input
            if event.type == pg.KEYDOWN:
                # r and esc only for when the game is over
                if event.key == pg.K_r and is_game_over:
                    game.restart()
                    is_game_over = False
                elif event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()

                if event.key == pg.K_LEFT:
                    game.map_cotrols("LEFT") 
                if event.key == pg.K_RIGHT:
                    game.map_cotrols("RIGHT") 
                if event.key == pg.K_UP:
                    game.map_cotrols("UP") 
                if event.key == pg.K_DOWN:
                    game.map_cotrols("DOWN")
                
                is_game_over = game.game_over()

        if not is_game_over:  
            game.create_display()
        else:
            game.display.reset_display()
            
        
        clock.tick(FPS)  # limits FPS to 60
        await asyncio.sleep(0)

    pg.quit()
    sys.exit()
asyncio.run(main())