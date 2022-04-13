
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = make_new_board()

        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in  range(self.dim_size) for _ in 
        ]]

def play(dim_size=10, num_boombs=10):
    pass
