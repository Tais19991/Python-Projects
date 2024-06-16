import unittest
from unittest.mock import patch
from board import Board
from player import Player
from main import Game


class TestBoard(unittest.TestCase):

    def setUp(self):
        """Set up a new board for each test"""
        self.board = Board()

    def test_initial_board(self):
        """Test the initial state of the board"""
        expected_board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.assertEqual(self.board.board, expected_board)
        self.assertIsNone(self.board.board_status)

    def test_is_moves_left_true(self):
        """Test is_moves_left returns True for a new board"""
        self.assertTrue(self.board.is_moves_left())

    def test_is_moves_left_false(self):
        """Test is_moves_left returns False for a full board"""
        self.board.board = [["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]]
        self.assertFalse(self.board.is_moves_left())

    def test_is_win_combination_row(self):
        """Test is_win_combination returns True for a winning row"""
        self.board.board = [["x", "x", "x"], ["_", "_", "_"], ["_", "_", "_"]]
        self.assertTrue(self.board.is_win_board_combination())

    def test_is_win_combination_column(self):
        """Test is_win_combination returns True for a winning column"""
        self.board.board = [["x", "_", "_"], ["x", "_", "_"], ["x", "_", "_"]]
        self.assertTrue(self.board.is_win_board_combination())

    def test_is_win_combination_diagonal(self):
        """Test is_win_combination returns True for a winning diagonal"""
        self.board.board = [["x", "_", "_"], ["_", "x", "_"], ["_", "_", "x"]]
        self.assertTrue(self.board.is_win_board_combination())

    def test_is_win_combination_antidiagonal(self):
        """Test is_win_combination returns True for a winning anti-diagonal"""
        self.board.board = [["_", "_", "x"], ["_", "x", "_"], ["x", "_", "_"]]
        self.assertTrue(self.board.is_win_board_combination())

    def test_check_board_draw(self):
        """Test check_board sets board_status to 'draw'"""
        self.board.board = [["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]]
        self.board.check_board()
        self.assertEqual(self.board.board_status, 'draw')

    def test_check_board_win(self):
        """Test check_board sets board_status to 'win'"""
        self.board.board = [["x", "x", "x"], ["_", "_", "_"], ["_", "_", "_"]]
        self.board.check_board()
        self.assertEqual(self.board.board_status, 'win')


class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up a new board and player for each test"""
        self.board = Board()
        self.player = Player('x', self.board)

    def test_player_initialization(self):
        """Test the player is initialized correctly"""
        self.assertEqual(self.player.player, 'x')
        self.assertEqual(self.player.board, self.board)
        self.assertEqual(self.player.row, 0)
        self.assertEqual(self.player.col, 0)

    @patch('builtins.input', side_effect=['0', '1'])
    def test_ask_player_move_valid(self, mock_input):
        """Test player move input is valid"""
        self.player.ask_player_move()
        self.assertEqual(self.player.row, 1)
        self.assertEqual(self.player.col, 0)

    def test_make_move(self):
        """Test making a move updates the board"""
        self.player.row, self.player.col = 1, 1
        self.player.make_move()
        self.assertEqual(self.board.board[1][1], 'x')

    def test_auto_find_next_move(self):
        """Test the auto move logic"""
        self.board.board = [
            ["x", "_", "o"],
            ["x", "x", "o"],
            ["o", "_", "_"]
        ]
        self.player.auto_find_next_move(opponent='o')
        self.player.make_move()
        self.assertEqual(self.board.board[2][2], 'x')

        # case 2
        self.board.board = [
            ["x", "_", "o"],
            ["x", "_", "_"],
            ["o", "x", "o"]
        ]
        self.player.auto_find_next_move(opponent='o')
        self.player.make_move()
        self.assertEqual(self.board.board[2][1], 'x')

        # case 3
        self.board.board = [
            ["_", "_", "o"],
            ["x", "x", "o"],
            ["o", "_", "_"]
        ]
        self.player.auto_find_next_move(opponent='o')
        self.player.make_move()
        self.assertEqual(self.board.board[2][2], 'x')  # Block the opponent's win




if __name__ == '__main__':
    unittest.main()
