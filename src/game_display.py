import pygame as pg
import sys
from constants import WIDTH, HEIGHT, BACKGROUND_COLOR, EMPTY_CELL_COLOR, TILE_IMAGES, FONT, SCORE_FONT

class Display:
    def __init__(self):
        pg.display.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Seal and Sea Lion 2048")
    
    def draw_grid(self, surface):
        surface.fill(pg.Color(BACKGROUND_COLOR))