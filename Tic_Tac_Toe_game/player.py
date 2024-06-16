from board import Board


class Player:
    def __init__(self, player, board: Board):
        self.player = player
        self.board = board
        self.row = 0
        self.col = 0

    def ask_player_move(self) -> None:
        """Prompt the player to input row and column numbers for their move."""
        while True:
            try:
                self.col = int(input('Choose number of column (0-2): '))
                self.row = int(input('Choose number of row (0-2): '))
                if 0 <= self.col <= 2 and 0 <= self.row <= 2:
                    if self.board.board[self.row][self.col] == '_':
                        break
                    else:
                        print('The place has been taken already. Choose another place to move')
                else:
                    print("Numbers must be between 0 and 2.")
            except ValueError:
                print('Invalid input. Please choose numbers between 0 and 2.')

    def make_move(self) -> None:
        """Update board after player move"""
        self.board.board[self.row][self.col] = self.player

    def auto_find_next_move(self, opponent) -> None:
        """Determine the best move for the computer player"""
        b = self.board.board

        # Check for winning move or block opponent's winning move
        for priority in (opponent, self.player):
            for row in range(3):
                for col in range(3):
                    if b[row][col] == '_':
                        b[row][col] = priority
                        if self.board.is_win_board_combination():
                            self.row, self.col = row, col
                            b[row][col] = '_'
                            return
                        b[row][col] = '_'

        # If no winning/blocking move found, pick the first available move
        for row in range(3):
            for col in range(3):
                if b[row][col] == '_':
                    self.row, self.col = row, col
                    return
