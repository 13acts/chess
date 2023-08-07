from pieces import *


EMT = None


def initial_positions():
    """
    Returns starting position of pieces
    """
    white = set()
    for i in range(6, 8):
        for j in range(0, 8):
            white.add((i, j))
    black = set()
    for i in range(0, 2):
        for j in range(0, 8):
            black.add((i, j))
    return {"white": white, "black": black}


def initial_pieces():
    """
    Returns starting states of pieces
    """
    active = initial_positions()
    white = {
        "KW": King((7, 4), active["black"]),
        "QW": Queen((7, 5), active["black"]),
        "RW1": Rook((7, 0), "L", active["black"]),
        "RW2": Rook((7, 7), "R", active["black"]),
        "BW1": Bishop((7, 2), active["black"]),
        "BW2": Bishop((7, 5), active["black"]),
        "NW1": Knight((7, 1), active["black"]),
        "NW2": Knight((7, 6), active["black"])
        }
    for x in range(1, 9):
        white[f"PW{x}"] = Pawn((6, x-1), "W", active["black"])

    black = {
        "KB": King((0, 4), active["white"]),
        "QB": Queen((0, 5), active["white"]),
        "RB1": Rook((0, 0), "L", active["white"]),
        "RB2": Rook((0, 7), "R", active["white"]),
        "BB1": Bishop((0, 2), active["white"]),
        "BB2": Bishop((0, 5), active["white"]),
        "NB1": Knight((0, 1), active["white"]),
        "NB2": Knight((0, 6), active["white"])
        }
    for x in range(1, 9):
        black[f"PB{x}"] = Pawn((1, x-1), "B", active["white"])

    return white, black


def initial_board(white, black):
    """
    Returns starting state of the board.
    """
    # Consider another approach: Assign pieces to class from this board
    # board = [["RB1", "NB1", "BB1", "QB" , "KB" , "BB2", "NB2", "RB2"],
    #         ["PB1", "PB2", "PB3", "PB4", "PB5", "PB6", "PB7", "PB8"],
    #         [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
    #         [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
    #         [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
    #         [EMT, EMT, EMT, EMT, EMT, EMT, EMT, EMT],
    #         ["PW1", "PW2", "PW3", "PW4", "PW5", "PW6", "PW7", "PW8"],
    #         ["RW1", "NW1", "BW1", "QW" , "KW" , "BW2", "NW2", "RW2"]
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


def active_pieces(white, black):
    """
    Returns positions of active pieces
    """
    active_white = set()
    for piece in white:
        active_white.add(white[piece].position)
    
    active_black = set()
    for piece in black:
        active_black.add(black[piece].position)

    return {"white": active_white, "black": active_black}


white, black = initial_pieces()
print(initial_board(white, black))
print(active_pieces(white, black)["white"])