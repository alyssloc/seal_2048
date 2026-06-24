import pygame as pg
class Controls:
    def __init___(self):
        x = 2
    
    def get_key_input(self) -> str:
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            return "LEFT"
        if keys[pg.K_RIGHT]:
            return "RIGHT"
        if keys[pg.K_UP]:
            return "UP"
        if keys[pg.K_DOWN]:
            return "DOWN"

        return "ERROR"

    def hit_restart(self) -> bool:
        return True

    def game_over_controls(self) -> str:
        return "yay"