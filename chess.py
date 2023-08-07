from pieces import *


EMT = None


def initial_board(white, black):
    """
    Returns starting state of the board.
    """
    # Consider another approach: Assign pieces to class from this board
    # board = [[RB1, NB1, BB1, QB , KB , BB2, NB2, RB2],
    #         [PB1, PB2, PB3, PB4, PB5, PB6, PB7, PB8],
    #         [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
    #         [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
    #         [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
    #         [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
    #         [PW1, PW2, PW3, PW4, PW5, PW6, PW7, PW8],
    #         [RW1, NW1, BW1, QW , KW , BW2, NW2, RW2]
    #         ]
    
    # Current approach: Assign pieces to board from class
    board = [[EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
            [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT]]
    
    for piece in white:
        i, j = white[piece].position
        board[i][j] = piece

    for piece in black:
        i, j = black[piece].position
        board[i][j] = piece
    
    return board


# Location of pieces
def get_W_positions(white):
    result = set()
    for piece in white:
        result.add(white[piece].position)
    return result

def get_B_positions(black):
    result = set()
    for piece in black:
        result.add(black[piece].position)
    return result


def initial_pieces():
    white = {
        "KW": King((7, 4), get_B_positions),
        "QW": Queen((7, 5), get_B_positions),
        "RW1": Rook((7, 0), "L", get_B_positions),
        "RW2": Rook((7, 7), "R", get_B_positions),
        "BW1": Bishop((7, 2), get_B_positions),
        "BW2": Bishop((7, 5), get_B_positions),
        "NW1": Knight((7, 1), get_B_positions),
        "NW2": Knight((7, 6), get_B_positions)
        }
    for x in range(1, 9):
        white[f"PW{x}"] = Pawn((6, x-1), "W", get_B_positions)

    black = {
        "KB": King((0, 4), get_W_positions),
        "QB": Queen((0, 5), get_W_positions),
        "RB1": Rook((0, 0), "L", get_W_positions),
        "RB2": Rook((0, 7), "R", get_W_positions),
        "BB1": Bishop((0, 2), get_W_positions),
        "BB2": Bishop((0, 5), get_W_positions),
        "NB1": Knight((0, 1), get_W_positions),
        "NB2": Knight((0, 6), get_W_positions)
        }
    for x in range(1, 9):
        black[f"PB{x}"] = Pawn((1, x-1), "B", get_W_positions)

    return white, black


white, black = initial_pieces()
print(initial_board(white, black))