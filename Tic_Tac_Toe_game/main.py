from player import Player
from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.end_game = False
        self.player = None
        self.opponent = None
        self.current_player = None

    def select_players(self):
        """Allow player 1 select symbol and auto-select player 2"""
        player1_symbol = input('\nSelect player (x or o): ').lower()
        while player1_symbol not in ['x', 'o']:
            print('\nWrong letter has been chosen')
            return self.select_players()
        self.player = Player(player1_symbol, self.board)
        # auto-selection player 2
        player2_symbol = 'o' if player1_symbol == 'x' else 'x'
        self.opponent = Player(player2_symbol, self.board)

    def switch_player(self):
        """Switch players between sessions"""
        self.current_player = self.opponent if self.current_player == self.player else self.player

    def choose_option(self):
        while True:
            try:
                option = int(input("\nChoose option:\n1 - Hot Seat (play with nearby human)\n2 - play with computer\n"))
                if option in [1, 2]:
                    return option
                print("\nWrong number has been chosen. Try again")
            except ValueError:
                print("\nInvalid input. Please enter 1 or 2.")

    def main(self):
        """Main program flow"""
        option = self.choose_option()
        self.select_players()
        self.current_player = self.opponent

        while not self.end_game:
            self.switch_player()
            print(f'\nPlayer {self.current_player.player} move:')

            if option == 1 or self.current_player == self.player:
                self.current_player.ask_player_move()
            else:
                self.current_player.auto_find_next_move(opponent=self.player)

            self.current_player.make_move()
            board_status = self.board.check_board()

            if board_status == 'win':
                print(f'\nCongrats, player {self.current_player.player} wins!')
                self.end_game = True
            elif board_status == 'draw':
                print("It's a draw!")
                self.end_game = True


if __name__ == '__main__':
    Game().main()
