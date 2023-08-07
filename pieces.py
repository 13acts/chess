class Pawn():
    def __init__(self, position, side, opponents):
        self.alive = True
        self.moved = False
        self.position = position
        self.side = side
        self.opponents = opponents

    def __str__(self):
        return f"P at {self.position}"

    def available_moves(self, board):
        # REMEMBER TO ONLY CALL AFTER PROMOTE CHECK
        result = set()
        x, y = self.position
        if self.side == "W":
            # 1 move ahead
            if board[x][y+1] is None:
                result.add((x, y+1))
                # 2 moves ahead
                if y + 2 < 8:
                    if not self.moved and board[x][y+2] is None:
                        result.add((x, y+2))
            # Can eat opponent piece
            if x + 1 < 8:
                if board[x+1][y+1] in self.opponents:
                    result.add((x+1, y+1))
            if x - 1 > -1:
                if board[x-1][y+1] in self.opponents:
                    result.add((x-1, y+1))
            # en passant
            ...
            return result
        
        elif self.side == "B":
            # 1 move ahead
            if board[x][y-1] is None:
                result.add((x, y-1))
                # 2 moves ahead
                if y - 2 > -1:
                    if not self.moved and board[x][y-2] is None:
                        result.add((x, y-2))
            # Can eat opponent piece
            if x + 1 < 8:
                if board[x+1][y-1] in self.opponents:
                    result.add((x+1, y-1))
            if x - 1 > -1:
                if board[x-1][y-1] in self.opponents:
                    result.add((x-1, y-1))
            # en passant
            ...
            return result

    def can_be_promoted(self):
        if self.side == "W":
            return self.position[1] == 7
        else:
            return self.position[1] == 0


class Rook():
    def __init__(self, position, half, opponents):
        self.alive = True
        self.moved = False
        self.position = position
        self.half = half
        self.opponents = opponents

    def __str__(self):
        return f"RW at {self.position}"

    def available_moves(self, board):
        result = set()
        x, y = self.position
        # Check on the right
        r = x + 1
        while r < 8:
            if board[r][y] is None:
                result.add((r, y))
            elif board[r][y] in self.opponents:
                result.add((r, y))
                break
            else:
                break
            r += 1
        # Check on the left
        l = x - 1
        while l > -1:
            if board[l][y] is None:
                result.add((l, y))
            elif board[l][y] in self.opponents:
                result.add((l, y))
                break
            else:
                break
            l -= 1
        # Check up
        u = y + 1
        while u < 8:
            if board[x][u] is None:
                result.add((x, u))
            elif board[x][u] in self.opponents:
                result.add((x, u))
                break
            else:
                break
            u += 1
        # Check down:
        d = y - 1
        while d > -1:
            if board[x][d] is None:
                result.add((x, d))
            elif board[x][d] in self.opponents:
                result.add((x, d))
                break
            else:
                break
            d -= 1
# Find a way to exclude this when inherited by Queen
        # Check castling
        if self.can_castle:
            result.add(self.can_castle)
        return result
    
    def can_castle(self, board, King_moved, KW_checked=False):
        # https://support.chess.com/article/266-how-do-i-castle
# Missing rule "Your king can not pass through check"
        y = self.position[1]
        if not self.moved and not King_moved:
            if self.half == "L":
                if any(board[x][y] for x in {1, 2, 3}):
                    return None
                return (3, y)
            else:
                if any(board[x][y] for x in {5, 6}):
                    return None
                return (5, y)
        else:
            return None
        

class Bishop():
    def __init__(self, position, opponents):
        self.alive = True
        self.position = position
        self.opponents = opponents

    def __str__(self):
        return f"BW at {self.position}"

    def available_moves(self, board):
        result = set()
        x, y = self.position
        # Check up right
        u = y + 1
        r = x + 1
        while u < 8 or r < 8:
            if board[r][u] is None:
                result.add((r, u))
            elif board[r][u] in self.opponents:
                result.add((r, u))
                break
            else:
                break
            u += 1
            r += 1
        # Check down right
        d = y - 1
        r = x + 1
        while d > -1 or r < 8:
            if board[r][d] is None:
                result.add((r, d))
            elif board[r][d] in self.opponents:
                result.add((r, d))
                break
            else:
                break
            d += 1
            r += 1
        # Check down left
        d = y - 1
        l = x - 1
        while d > -1 or l > -1:
            if board[l][d] is None:
                result.add((l, d))
            elif board[r][d] in self.opponents:
                result.add((l, d))
                break
            else:
                break
            d += 1
            l += 1
        # Check up left
        u = y + 1
        l = x - 1
        while u < 8 or l > -1:
            if board[l][u] is None:
                result.add((r, d))
            elif board[l][u] in self.opponents:
                result.add((l, u))
                break
            else:
                break
            u += 1
            l += 1


class Knight():
    def __init__(self, position):
        self.alive = True
        self.position = position

    def __str__(self):
        return f"NW at {self.position}"

    def available_moves(self, board, white_pieces):
        x, y = self.position
        result = set((x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2),
                  (x-1, y-2), (x-2, y-1), (x-2, y+1), (x-1, y+2))
        for move in result:
            try:
                if board[move[0]][move[1]] in white_pieces:
                    result.remove(move)
            except:
                pass
        return result


class Queen(Rook, Bishop):
    def __init__(self, position, opponents):
        self.alive = True
        self.position = position
        self.opponents = opponents

    def __str__(self):
        return f"Q at {self.position}"

    def available_moves(self, board):
        straight = Rook.available_moves(board, self.opponents)
        diagonal = Bishop.available_moves(board, self.opponents)
        return straight.union(diagonal)
    

class King():
    def __init__(self, position, opponents):
        self.alive = True
        self.moved = False
        self.position = position
        self.opponents = opponents

    def __str__(self):
        return f"K at {self.position}"
    
    def available_moves(self, board):
        result = set()
        x, y = self.position
        # Normal case
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                try:
                    if board[i][j] is None:
                        result.add((i, j))
                    elif board[i][j] in self.opponents:
                        result.add((i, j))
                    else:
                        continue
                except:
                    pass
        # Castling
        if len(self.can_castle) != 0:
            result.union(self.can_castle)

    def can_castle(self, board, KnightL_moved, KnightR_moved):
        # https://support.chess.com/article/266-how-do-i-castle
# Missing rule "Your king can not pass through check"
        result = set()
        y = self.position[1]
        if not self.moved and not KnightL_moved:
            if not any(board[x][y] for x in {1, 2, 3}):
                result.add((2, y))
        if not self.moved and not KnightR_moved:
            if not any(board[x][y] for x in {5, 6}):
                result.add((6, y))
        return result