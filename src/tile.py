class Tile:
    val: int
    
    def __init__(self, val: int) -> None:
        self.val = val
    
    def set_val(self, val_in: int) -> None:
        self.val = val_in

    def merge(self) -> None:
        self.val *= 2
    
    def is_empty(self) -> bool:
        return self.val == 0