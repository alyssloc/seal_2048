import pygame as pg
import sys
from constants import WIDTH, HEIGHT, CELL_SIZE, BACKGROUND_COLOR, DARK_BLUE, WHITE, TILE_IMAGES, FONT, SCORE_FONT, GAME_OVER_FONT

class Display:
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    restart_button_rect = pg.Rect(10, 45, 80, 35)

    def __init__(self):
        pg.display.init()
        self.screen.fill(BACKGROUND_COLOR)
        pg.display.set_caption("Seal and Sea Lion 2048")
    
    def draw_square(self, val: int, r: int, c: int) -> None:
        image = TILE_IMAGES[val]
        x = c * CELL_SIZE
        y = r * CELL_SIZE
        self.screen.blit(image, (x, y))
    
    def update_score(self, score_in: int) -> None:
        score_text = SCORE_FONT.render(f"Score: {score_in}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
    
    def reset_display(self) -> None:
        pg.display.flip()
    
    def display_game_over(self) -> None:
        go_text = GAME_OVER_FONT.render("GAME OVER", True, DARK_BLUE)
        go_rect = go_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        self.screen.blit(go_text, go_rect)
        sub_text = SCORE_FONT.render("Press 'R' to Restart or 'ESC' to Quit", True, WHITE)
        sub_rect = sub_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
        self.screen.blit(sub_text, sub_rect)
    
    def display_restart_button(self) -> None:
        btn_text = SCORE_FONT.render("Restart", True, (255, 255, 255))
        self.screen.blit(btn_text, btn_text.get_rect(center = self.restart_button_rect.center))