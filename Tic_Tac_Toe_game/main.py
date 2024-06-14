from auto_player import AutoPlayer, AiPlayer


def show_board(current_board) -> None:
    """Shows pretty board"""
    print('\n' + '\n'.join(['\t'.join([str(cell) for cell in row]) for row in current_board]))
    print('\n' + '*' * 32 + '\n')


def update_board(board, row_num: int, col_num: int, player: str) -> list:
    """Updates board after player move"""
    board[row_num][col_num] = player
    return board


def is_valid_move(board, row_num: int, col_num: int):
    """Checks whether the player has chosen the correct move"""
    if 0 <= row_num <= 2 and 0 <= col_num <= 2:
        if board[row_num][col_num] == '_':
            return True
        else:
            print('The place has been taken already. Choose another place to move')
            return False
    else:
        print("Chosen number is out of range")
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


def is_moves_left(board) -> bool:
    """Takes the board and check if moves remaining on the board"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False


def select_player():
    """Defines players x and o"""
    player = input('\nSelect player (x or o):\n').lower()
    if player in ['x', 'o']:
        opponent = 'o' if player == 'x' else 'x'
        return player, opponent
    else:
        print('\nWrong letter has been chosen\n')
        return select_player()


def user_move() -> tuple:
    """Ask user about x,o position and return number of row and col on board"""
    try:
        col = int(input('\nChoose number of column (0-2):\n'))
        row = int(input('Choose number of row (0-2):\n'))
    except ValueError:
        print('Incorrect symbol. Choose number of row (0, 1, 2) and number of column (0, 1, 2)')
        return user_move()
    else:
        return row, col


def switch_user(users: tuple, current_player_flag: bool):
    """Switch users between sessions"""
    return users[0] if current_player_flag else users[1], not current_player_flag


def main():
    """Main program flow"""

    board = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]
    end_game = False
    chosen_option = int(input("\nChoose option:\n1 - Hot Seat (play with nearby human)\n2 - play with computer\n"))
    player, opponent = select_player()
    current_player_flag = False
    current_player = player
    row, col = 0, 0

    while not end_game:

        # state of board
        show_board(board)
        # your move
        print(f'Player {current_player} move:')

        valid_move = False
        while not valid_move:
            # game with human
            if chosen_option == 1:
                row, col = user_move()

            # game with autoplay
            elif chosen_option == 2:
                if current_player == player:
                    row, col = user_move()
                else:
                    comp = AiPlayer(board, opponent)
                    row, col = comp.find_next_move()

            # check validity of move
            valid_move = is_valid_move(board, row, col)

        # update board
        update_board(board, row, col, current_player)

        # check win, draw and end of game
        if win_checker(board):
            show_board(board)
            print(f'\nCongrats, player {current_player} win!')
            end_game = True
        elif not is_moves_left(board):
            show_board(board)
            print("It's draw!")
            end_game = True
        else:
            # change player
            current_player, current_player_flag = switch_user((player, opponent), current_player_flag)


if __name__ == '__main__':
    main()
