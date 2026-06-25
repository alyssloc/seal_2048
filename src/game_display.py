import pygame as pg
from constants import (CELL_SIZE, GRID_SIZE, WIDTH, HEIGHT, GREEN, RED, BACKGROUND_COLOR, SEAL_BACKGROUND_COLORS, SEAL_NAMES, 
                        DARK_BLUE, WHITE, TILE_IMAGES, FONT, SCORE_FONT, GAME_OVER_FONT, KEY_FONT, YELLOW)

class Display:
    def __init__(self):
        pg.display.init()
        self.width = WIDTH
        self.height = HEIGHT

        self.screen = pg.display.set_mode((self.width, self.height))
        self.screen.fill(BACKGROUND_COLOR)
        pg.display.set_caption("Seal and Sea Lion 2048")

        # display will have game board to the left, key on the right (menu to view)
        self.board_total_size = GRID_SIZE * CELL_SIZE
        self.board_x = (self.width - self.board_total_size) // 2
        self.board_y = (self.height - self.board_total_size) // 2

        # restart and view key buttons
        self.restart_button_rect = pg.Rect(self.board_x + self.board_total_size - 100, self.board_y - 45, 100, 35)
        self.view_key_button_rect = pg.Rect(self.board_x + self.board_total_size - 240, self.board_y - 45, 130, 35)
        self.show_key = False
        self.close_button_rect = pg.Rect(0, 0, 0, 0)
    

    def draw_square(self, val: int, r: int, c: int) -> None:
        x = self.board_x + (c * CELL_SIZE)
        y = self.board_y + (r * CELL_SIZE)

        # getting background color from color map for each tile
        bg_color = SEAL_BACKGROUND_COLORS.get(val, WHITE)

        pg.draw.rect(self.screen, bg_color, (x, y, CELL_SIZE, CELL_SIZE))
        pg.draw.rect(self.screen, DARK_BLUE, (x, y, CELL_SIZE, CELL_SIZE), width=3)

        if val != 0:
            image = TILE_IMAGES[val]
            self.screen.blit(image, (x, y))
    
    def update_score(self, score_in: int) -> None:
        pg.draw.rect(self.screen, BACKGROUND_COLOR, (self.board_x, self.board_y - 50, 200, 40))
        score_text = SCORE_FONT.render(f"Score: {score_in}", True, WHITE)
        self.screen.blit(score_text, (self.board_x, self.board_y - 45))
    
    def draw_key(self) -> None:
        # only display the key when the user hits the button
        if not self.show_key:
            return
        
        overlay_w, overlay_h = 640, 1000
        overlay_x = (self.width - overlay_w) // 2
        overlay_y = (self.height - overlay_h) // 2

        pg.draw.rect(self.screen, DARK_BLUE, (overlay_x, overlay_y, overlay_w, overlay_h), border_radius=12)
        pg.draw.rect(self.screen, WHITE, (overlay_x, overlay_y, overlay_w, overlay_h), width=4, border_radius=12)

        title_text = FONT.render("Key", True, WHITE)
        self.screen.blit(title_text, (overlay_x + 40, overlay_y + 25))

        # close button when key is open
        self.close_button_rect = pg.Rect(overlay_x + overlay_w - 140, overlay_y + 25, 100, 35)
        pg.draw.rect(self.screen, BACKGROUND_COLOR, self.close_button_rect, border_radius=5)
        pg.draw.rect(self.screen, WHITE, self.close_button_rect, width=2, border_radius=5)
        close_text = SCORE_FONT.render("Close", True, WHITE)
        self.screen.blit(close_text, close_text.get_rect(center=self.close_button_rect.center))

        # 3 x 5 grid for displaying seals
        seal_values = sorted([k for k in TILE_IMAGES.keys() if k != 0])
        start_x = overlay_x + 40
        start_y = overlay_y + 95
        row_height = 110
        thumb_size = 80
        column_width = 280

        for i, val in enumerate(seal_values):
            col = i % 2
            row = i // 2

            x_pos = start_x + (col * column_width)
            y_pos = start_y + (row * row_height)

            bg_color = SEAL_BACKGROUND_COLORS.get(val, WHITE)

            pg.draw.rect(self.screen, bg_color, (x_pos, y_pos, thumb_size, thumb_size), border_radius=6)
            mini_seal = pg.transform.scale(TILE_IMAGES[val], (thumb_size, thumb_size))
            self.screen.blit(mini_seal, (x_pos, y_pos))

            # label: name of seal, its number, and its photo
            seal_label_string = f"{val}: {SEAL_NAMES.get(val, 'Unknown')}"
            label_text = KEY_FONT.render(seal_label_string, True, WHITE)
            text_y = y_pos + (thumb_size // 2) - (label_text.get_height() // 2)
            self.screen.blit(label_text, (x_pos + thumb_size + 12, text_y))

    
    def reset_display(self) -> None:
        if self.show_key:
            self.draw_key()
        pg.display.flip()
    
    def display_game_over_or_win(self, winner: bool) -> None:
        if winner:
            go_text = GAME_OVER_FONT.render("You Win!!!", True, GREEN)
        else:
            go_text = GAME_OVER_FONT.render("GAME OVER", True, RED)

        go_rect = go_text.get_rect(center=(self.width//2, self.height//2 - 50))
        self.screen.blit(go_text, go_rect)
        sub_text = SCORE_FONT.render("Press 'R' to Restart or 'ESC' to Quit", True, YELLOW)
        sub_rect = sub_text.get_rect(center=(self.width//2, self.height//2 + 50))
        self.screen.blit(sub_text, sub_rect)
    
    
    def display_restart_button(self) -> None:
        pg.draw.rect(self.screen, DARK_BLUE, self.restart_button_rect, border_radius=5)
        btn_text = SCORE_FONT.render("Restart", True, WHITE)
        self.screen.blit(btn_text, btn_text.get_rect(center=self.restart_button_rect.center))
    
    def display_key_button(self) -> None:
        pg.draw.rect(self.screen, DARK_BLUE, self.view_key_button_rect, border_radius=5)
        btn_text = SCORE_FONT.render("View Key", True, WHITE)
        self.screen.blit(btn_text, btn_text.get_rect(center=self.view_key_button_rect.center))
    
    def handle_key_click(self, mouse_pos) -> None:
        # opening key
        if self.view_key_button_rect.collidepoint(mouse_pos):
            self.show_key = not self.show_key
            if not self.show_key:
                self.screen.fill(BACKGROUND_COLOR) 

        # closing key
        if self.show_key and self.close_button_rect.collidepoint(mouse_pos):
            self.show_key = False
            self.screen.fill(BACKGROUND_COLOR) 
