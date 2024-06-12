from auto_player import AutoPlayer

board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]


def show_board(current_board) -> None:
    """Shows pretty board"""
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in current_board]) + '\n')


def update_board(board, row_num: int, col_num: int, player: str) -> list:
    """Updates board after player move"""
    if is_valid_move(board, row_num, col_num):
        board[row_num - 1][col_num - 1] = player
    return board


def is_valid_move(board, row_num: int, col_num: int) -> bool:
    """Checks whether the player has chosen the correct move"""
    if 1 <= row_num <= 3 and 1 <= col_num <= 3:
        if board[row_num - 1][col_num - 1] == '_':
            return True
        else:
            print('The place has been taken already. Choose another place to move')
            return False
    else:
        print('Incorrect numbers. Choose number of row (1-3) and number of column (1-3)')
        return False


def win_checker(board) -> bool:
    """Checks rows for a win combination"""
    for row in board:
        if row == ["x", "x", "x"] or row == ["o", "o", "o"]:
            return True

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ["x", "o"]:
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ["x", "o"]:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ["x", "o"]:
        return True

    # Check a draw
    if "_" not in board:
        print("Draw")
        return True


def select_player():
    player = input('\nSelect player (x or o):\n').lower()
    if player in ['x', 'o']:
        opponent = 'o' if player == 'x' else 'x'
        return player, opponent
    else:
        print('\nWrong letter has been chosen\n')
        return select_player()


def main():
    end_game = False
    chosen_option = int(input("\nChoose option:\n" \
                              "1 - hot seat (play with nearby human)\n" \
                              "2 - play with computer\n"))
    player, opponent = select_player()

    while not end_game:
        if chosen_option == 1:
            pass
        elif chosen_option == 2:
            pass


if __name__ == '__main__':
    main()
