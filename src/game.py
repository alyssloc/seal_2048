from board import Board
class Game:
    board: Board
    score: int

    def __init__(self):
        self.score = 0; 

    def move_left(self) -> None:
        self.board.slide_left()

    def move_right(self) -> None:
        self.board.reverse_rows()
        self.board.slide_left()
        self.board.reverse_rows()
    
    def move_up(self) -> None:
        self.board.transpose()
        self.board.slide_left()
        self.board.transpose()
    
    def move_down(self) -> None:
        self.board.transpose()
        self.board.reverse_rows()
        self.board.slide_left()
        self.board.reverse_rows()
        self.board.transpose()

    def game_over(self) -> None:
        # check if there are any empty tiles
        if self.board.check_for_game_over():
            x = 2
        