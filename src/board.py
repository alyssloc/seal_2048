from constants import GRID_SIZE
from tile import Tile
import random

class Board:
    grid: list[list[Tile]]
    
    def __init__(self):
        self.reset()
    
    def reset(self) -> None:
        # creating 4 x 4 matrix of Tile objects (all initially set to 0)
        self.grid = [[Tile(0) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        # setting two random tiles to start at 2/4
        self.generate_new_tile()
        self.generate_new_tile()
    
    def generate_new_tile(self) -> None: 
        # new tiles have a 90% chance of being 2, 10% chance of being 4
        options = [2, 4]
        probabilities = [0.9, 0.1]

        # selecting a random tile where val == 0 to become 2 or 4
        empty_tiles = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if self.grid[r][c].is_empty()]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            self.grid[r][c].set_val(random.choices(options, weights=probabilities, k=1)[0])

    def compress_row(self, r: int) -> None:
        # format rows to be empty tiles followed by non-empty tiles
        for _ in range(GRID_SIZE - 1):
            for c in range(0, GRID_SIZE - 1):
                if self.grid[r][c].is_empty() and not self.grid[r][c + 1].is_empty():
                    self.grid[r][c], self.grid[r][c + 1] = self.grid[r][c + 1], self.grid[r][c]

    def merge_row(self, r: int) -> int:
        # if there are two equal tiles next to each other, the right tile will merge, 
        # and the left will become zero
        points: int = 0; 
        for c in range(0, GRID_SIZE - 1):
            if self.grid[r][c].val == self.grid[r][c + 1].val:
                self.grid[r][c].merge()
                points += self.grid[r][c].val
                self.grid[r][c + 1].set_val(0)

        # after done merging, compress row
        self.compress_row(r)
        return points

    def slide_left(self) -> int:
        points: int = 0
        for r in range(GRID_SIZE):
            self.compress_row(r)
            points += self.merge_row(r)
        return points

    
    # reverse and transpose functions to be able to use slide_left function for all directions
    def reverse_rows(self) -> None:
        self.grid = [row[::-1] for row in self.grid]
    
    def transpose(self) -> None:
        self.grid = [list(row) for row in zip(*self.grid)]
    
    def check_for_game_over(self) -> bool:
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                # if empty spots: game not over
                if self.grid[r][c].is_empty():
                    return False
                # if possible horizontal/vertical move: game not over
                if c < GRID_SIZE - 1 and self.grid[r][c].val == self.grid[r][c + 1].val:
                    return False
                if r < GRID_SIZE - 1 and self.grid[r][c].val == self.grid[r + 1][c].val:
                    return False
                
        return True

    def move_down(self) -> int:
        self.transpose()
        self.reverse_rows()
        points: int = self.slide_left()
        self.reverse_rows()
        self.transpose()
        return points
    
    def move_left(self) -> int:
        return self.slide_left()

    def move_right(self) -> int:
        self.reverse_rows()
        points: int = self.slide_left()
        self.reverse_rows()
        return points
    
    def move_up(self) -> int:
        self.transpose()
        points: int = self.slide_left()
        self.transpose()
        return points