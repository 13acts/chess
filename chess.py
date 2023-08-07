from pieces import *


EMT = None # represents empty
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[RB1, NB1, BB1, QB , KB , BB2, NB2, RB2],
            [PB1, PB2, PB3, PB4, PB5, PB6, PB7, PB8],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [PW1, PW2, PW3, PW4, PW5, PW6, PW7, PW8],
            [RW1, NW1, BW1, QW , KW , BW2, NW2, RW2]
            ]
# Location of pieces
white_pieces = set()
for i in range(0, 8):
    for j in range(6, 8):

black_pieces = set()

# white pieces
KW = King() # represents white king
QW = Queen() # represents white queen 
RW1 = Rook() # represents white rook 
RW2 = Rook() # represents white rook 
BW1 = Bishop() # represents white bishop 
BW2 = Bishop() # represents white bishop 
NW1 = Knight() # represents white knight
NW2 = Knight() # represents white knight

# black pieces
PB = " ♟︎ " # represents black pawn
KB = " ♚ " # represents black king
QB = " ♛ " # represents black queen 
RB = " ♜ " # represents black rook 
BB = " ♝ " # represents black bishop 
NB = " ♞ " # represents black knight
BLACK = "BLACK" 
WHITE = "WHITE"