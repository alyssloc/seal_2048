from board import Board
from game_display import Display
from game_controls import Controls
from constants import GRID_SIZE

class Game:
    board: Board
    score: int
    display: Display
    controls: Controls

    def __init__(self):
        self.score = 0; 

    def game_over(self) -> bool:
        # check if there are any empty tiles
        if self.board.check_for_game_over():
            self.display.display_game_over()

            next_action: str = self.controls.game_over_controls()
            if next_action == "RESTART":
                self.restart()
            elif next_action == "QUIT":
                return False
        return True


    
    def create_display(self) -> None:
        for r in range(0, GRID_SIZE):
            for c in range(0, GRID_SIZE):
                self.display.draw_square(self.board.grid[r][c].val, r, c)
        self.display.update_score(self.score)
        self.display.display_restart_button()

        self.display.reset_display()

    
    def restart(self) -> None:
        self.board.reset()
        self.score = 0
        self.create_display()
    
    def map_cotrols(self) -> None:
        input: str = self.controls.get_key_input()
        
        if input == "LEFT":
            self.board.move_left()
        elif input == "RIGHT":
            self.board.move_right()
        elif input == "UP":
            self.board.move_up()
        elif input == "DOWN":
            self.board.move_down()
