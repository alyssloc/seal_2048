from board import Board
from game_display import Display
from constants import GRID_SIZE

class Game:
    board: Board
    score: int
    display: Display

    def __init__(self):
        self.score = 0; 
        self.display = Display()
        self.board = Board()

    def game_over(self) -> bool:
        # check if player won the game
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if self.board.grid[r][c].val == 32768:
                    self.display.display_game_over_or_win(True) 
                    return True
        # check if there are any empty tiles & return true if game is over
        if self.board.check_for_game_over():
            self.display.display_game_over_or_win(False)
            return True
        #false if game keeps going
        return False

    
    def create_display(self) -> None:
        #self.display.screen.fill((70, 30, 180))
        for r in range(0, GRID_SIZE):
            for c in range(0, GRID_SIZE):
                self.display.draw_square(self.board.grid[r][c].val, r, c)
        self.display.update_score(self.score)
        self.display.display_restart_button()
        self.display.display_key_button()
        self.display.reset_display()

    
    def restart(self) -> None:
        self.board.reset()
        self.score = 0
        self.create_display()
    
    def map_cotrols(self, input: str) -> None:
        old_grid = [[self.board.grid[r][c].val for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]
        if input == "LEFT":
            self.score += self.board.move_left()
        elif input == "RIGHT":
            self.score += self.board.move_right()
        elif input == "UP":
            self.score += self.board.move_up()
        elif input == "DOWN":
            self.score += self.board.move_down()
        
        # generating new tiles only if a valid move happened
        new_grid = [[self.board.grid[r][c].val for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]
        if old_grid != new_grid:
            self.board.generate_new_tile()
