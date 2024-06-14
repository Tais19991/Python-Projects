class AiPlayer:
    """Class for predicting the best opponent's move in a game of tic-tac-toe"""

    def __init__(self, board: list, opponent: str) -> None:
        self.board = board
        self.opponent = opponent

    def __repr__(self) -> str:
        return f'AI_player(board: {self.board}, ' \
               f'mark: {self.opponent})'

    def find_next_move(self) -> tuple:
        """Takes the state of the board, players(x, o) and determines the presence/absence of a winning combination"""
        b = self.board
        row_move = 0
        col_move = 0
        move = False

        while not move:

            # Checking for Rows
            for row in range(3):
                if b[row][0] == b[row][1] != self.opponent:
                    if b[row][2] == '_':
                        row_move = row
                        col_move = 2
                        move = True

                elif b[row][1] == b[row][2] != self.opponent:
                    if b[row][0] == '_':
                        row_move = row
                        col_move = 0
                        move = True

            # Checking for Columns
            for col in range(3):
                if b[0][col] == b[1][col] != self.opponent:
                    if b[2][col] == '_':
                        row_move = 2
                        col_move = col
                        move = True

                elif b[1][col] == b[2][col] != self.opponent:
                    if b[0][col] == '_':
                        row_move = 0
                        col_move = col
                        move = True

            # Checking for Diagonals for X or O victory.
            if b[0][0] == b[1][1] != self.opponent:
                if b[2][2] == '_':
                    row_move = 2
                    col_move = 2
                    move = True

            elif b[1][1] == b[2][2] != self.opponent:
                if b[0][0] == '_':
                    row_move = 0
                    col_move = 0
                    move = True

            elif b[0][2] == b[1][1] != self.opponent:
                if b[2][0] == '_':
                    row_move = 2
                    col_move = 0
                    move = True

            elif b[1][1] == b[2][0] != self.opponent:
                if b[0][2] == '_':
                    row_move = 0
                    col_move = 2
                    move = True

            else:
                for i in range(3):
                    for j in range(3):
                        if b[i][j] == '_':
                            row_move = i
                            col_move = j
                            move = True

        return row_move, col_move





class AutoPlayer():
    """Class for predicting the best opponent's move in a game of tic-tac-toe"""

    def __init__(self, board: list, player: str, opponent: str) -> None:
        self.board = board
        self.player = player
        self.opponent = opponent

    def __repr__(self) -> str:
        return f'AI_player(board: {self.board}, ' \
               f'player: {self.player},' \
               f'AI : {self.opponent})'

    def is_moves_left(self) -> bool:
        """Takes the board and check if moves remaining on the board"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    return True
        return False

    def evaluate(self) -> int:
        """Takes the state of the board, players(x, o) and determines the presence/absence of a winning combination"""
        b = self.board
        # Checking for Rows for X or O victory.
        for row in range(3):
            if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
                if b[row][0] == self.player:
                    return 10
                elif b[row][0] == self.opponent:
                    return -10

        # Checking for Columns for X or O victory.
        for col in range(3):

            if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

                if b[0][col] == self.player:
                    return 10
                elif b[0][col] == self.opponent:
                    return -10

        # Checking for Diagonals for X or O victory.
        if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

            if b[0][0] == self.player:
                return 10
            elif b[0][0] == self.opponent:
                return -10

        if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

            if b[0][2] == self.player:
                return 10
            elif b[0][2] == self.opponent:
                return -10

        # Else if none of them have won then return 0
        return 0

    #
    def minimax(self, board: list, depth: int, is_max: bool):
        """Estimate all the possible ways the game can go and return the value of the board"""
        score = self.evaluate()

        # If Maximizer has won the game return score
        if score == 10:
            return score

        # If Minimizer has won the game return  score
        if score == -10:
            return score

        # If there are no more moves and no winner then it is a tie
        if not self.is_moves_left():
            return 0

        # If this maximizer's move
        if is_max:
            best = -1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if self.board[i][j] == '_':
                        # Make the move
                        self.board[i][j] = self.player

                        # Call minimax recursively and choose the maximum value
                        best = max(best, self.minimax(self.board,
                                                      depth + 1,
                                                      not is_max))

                        # Undo the move
                        board[i][j] = '_'
            return best

        # If this minimizer's move
        else:
            best = 1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if self.board[i][j] == '_':
                        # Make the move
                        board[i][j] = self.opponent

                        # Call minimax recursively and choose the minimum value
                        best = min(best, self.minimax(self.board, depth + 1, not is_max))

                        # Undo the move
                        board[i][j] = '_'
            return best

    def find_best_move(self) -> tuple:
        """Takes board and return the best possible move for the player"""
        best_val = -1000
        best_move = (-1, -1)

        # Traverse all cells and return the cell with optimal  value.
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if self.board[i][j] == '_':

                    # Make the move
                    self.board[i][j] = self.player

                    # compute evaluation function for this move.
                    move_val = self.minimax(self.board, 0, False)

                    # Undo the move
                    self.board[i][j] = '_'

                    # If the value of the current move is more than the best value, then update
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val

        return best_move
