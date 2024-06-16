class Board:
    def __init__(self):
        self.board = [["_", "_", "_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]
        self.board_status = None

    def show_board(self) -> None:
        """Show pretty board"""
        print('\n' + '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
        print('\n' + '*' * 32)

    def is_moves_left(self) -> bool:
        """Check if moves remaining on the board"""
        return any(cell == '_' for row in self.board for cell in row)

    def is_win_board_combination(self) -> bool:
        """Check rows, columns, and diagonals for a win combination"""
        lines = self.board + [list(col) for col in zip(*self.board)]  # Rows and columns
        lines.append([self.board[i][i] for i in range(3)])  # Main diagonal
        lines.append([self.board[i][2 - i] for i in range(3)])  # Anti-diagonal
        return any(line == ['x', 'x', 'x'] or line == ['o', 'o', 'o'] for line in lines)

    def check_board(self):
        """Check board status - win or draw"""
        self.show_board()
        # win
        if self.is_win_board_combination():
            self.board_status = 'win'
        # draw
        elif not self.is_moves_left():
            self.board_status = 'draw'
        return self.board_status
