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
        i, j = self.position
        if self.side == "W":
            # 1 move ahead
            if board[i+1][j] is None:
                result.add((i+1, j))
                # 2 moves ahead
                if i + 2 < 8:
                    if not self.moved and board[i+2][j] is None:
                        result.add((i+2, j))
            # Can eat opponent piece
            if j + 1 < 8:
                if board[i+1][j+1] in self.opponents:
                    result.add((i+1, j+1))
            if j - 1 > -1:
                if board[i+1][j-1] in self.opponents:
                    result.add((i+1, j-1))
            # en passant
            ...
            return result
        
        elif self.side == "B":
            # 1 move ahead
            if board[i-1][j] is None:
                result.add((i-1, j))
                # 2 moves ahead
                if i - 2 > -1:
                    if not self.moved and board[i-2][j] is None:
                        result.add((i-2, j))
            # Can eat opponent piece
            if j + 1 < 8:
                if board[i-1][j+1] in self.opponents:
                    result.add((i-1, j+1))
            if j - 1 > -1:
                if board[i-1][j-1] in self.opponents:
                    result.add((i-1, j-1))
            # en passant
            ...
            return result

    def can_be_promoted(self):
        if self.side == "W":
            return self.position[0] == 7
        else:
            return self.position[0] == 0


class Rook():
    def __init__(self, position, half, opponents):
        self.alive = True
        self.moved = False
        self.position = position
        self.half = half
        self.opponents = opponents

    def __str__(self):
        return f"R at {self.position}"

    def available_moves(self, board):
        result = set()
        i, j = self.position
        # Check up
        r = i + 1
        while r < 8:
            if board[r][j] is None:
                result.add((r, j))
            elif board[r][j] in self.opponents:
                result.add((r, j))
                break
            else:
                break
            r += 1
        # Check down
        d = i - 1
        while d > -1:
            if board[d][j] is None:
                result.add((d, j))
            elif board[d][j] in self.opponents:
                result.add((d, j))
                break
            else:
                break
            d -= 1
        # Check right
        r = j + 1
        while r < 8:
            if board[i][r] is None:
                result.add((i, r))
            elif board[i][r] in self.opponents:
                result.add((i, r))
                break
            else:
                break
            r += 1
        # Check left:
        l = j - 1
        while l > -1:
            if board[i][d] is None:
                result.add((i, d))
            elif board[i][d] in self.opponents:
                result.add((i, d))
                break
            else:
                break
            l -= 1
# Find a way to exclude this when inherited by Queen
        # Check castling
        if self.can_castle:
            result.add(self.can_castle)
        return result
    
    def can_castle(self, board, King_moved, KW_checked=False):
        # https://support.chess.com/article/266-how-do-i-castle
# Missing rule "Your king can not pass through check"
        i = self.position[0]
        if not self.moved and not King_moved:
            if self.half == "L":
                if any(board[i][j] for j in {1, 2, 3}):
                    return None
                return (i, 3)
            else:
                if any(board[i][j] for j in {5, 6}):
                    return None
                return (i, 5)
        else:
            return None
        

class Bishop():
    def __init__(self, position, opponents):
        self.alive = True
        self.position = position
        self.opponents = opponents

    def __str__(self):
        return f"B at {self.position}"

    def available_moves(self, board):
        result = set()
        i, j = self.position
        # Check up right
        d = i + 1
        r = j + 1
        while d < 8 or r < 8:
            if board[d][r] is None:
                result.add((d, r))
            elif board[d][r] in self.opponents:
                result.add((d, r))
                break
            else:
                break
            d += 1
            r += 1
        # Check down right
        d = i - 1
        r = j + 1
        while d > -1 or r < 8:
            if board[d][r] is None:
                result.add((d, r))
            elif board[d][r] in self.opponents:
                result.add((d, r))
                break
            else:
                break
            d -= 1
            r += 1
        # Check down left
        d = i - 1
        l = j + 1
        while d > -1 or l > -1:
            if board[d][l] is None:
                result.add((d, l))
            elif board[d][l] in self.opponents:
                result.add((d, l))
                break
            else:
                break
            d -= 1
            l -= 1
        # Check up left
        u = i + 1
        l = j - 1
        while u < 8 or l > -1:
            if board[u][l] is None:
                result.add((u, l))
            elif board[u][l] in self.opponents:
                result.add((u, l))
                break
            else:
                break
            u += 1
            l -= 1


class Knight():
    def __init__(self, position, opponents):
        self.alive = True
        self.position = position
        self.opponents = opponents

    def __str__(self):
        return f"N at {self.position}"

    def available_moves(self, board):
        i, j = self.position
        result = set((i+1, j+2), (i+2, j+1), (i+2, j-1), (i+1, j-2),
                  (i-1, j-2), (i-2, j-1), (i-2, j+1), (i-1, j+2))
        for move in result:
            try:
                if board[move[0]][move[1]] in self.opponents:
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
        i, j = self.position
        # Normal case
        for i in range(i-1, i+2):
            for j in range(j-1, j+2):
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
        i = self.position[0]
        if not self.moved and not KnightL_moved:
            if not any(board[i][j] for j in {1, 2, 3}):
                result.add((i, 2))
        if not self.moved and not KnightR_moved:
            if not any(board[i][j] for j in {5, 6}):
                result.add((i, 6))
        return result