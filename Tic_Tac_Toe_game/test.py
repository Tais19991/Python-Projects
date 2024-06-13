import unittest
from main import win_checker, is_moves_left


class MyTestCase(unittest.TestCase):
    def test_win_combinations(self):
        """test win combinations"""
        board = [['x', 'o', 'x'],
                 ['o', 'o', 'x'],
                 ['o', 'x', 'x']]

        board2 = [['x', 'o', 'x'],
                  ['o', 'x', 'o'],
                  ['o', 'x', 'x']]
        x = win_checker(board)
        y = win_checker(board2)
        self.assertEqual(x, True)
        self.assertEqual(y, True)

    def test_left_moves(self):
        """test win and draw combinations"""
        board = [['x', 'o', 'x'],
                 ['o', 'o', 'x'],
                 ['o', 'x', 'o']]
        board2 = [['x', 'o', 'x'],
                  ['o', 'o', 'x'],
                  ['o', '_', '_']]
        x = is_moves_left(board)
        y = is_moves_left(board2)
        self.assertEqual(y, True)
        self.assertFalse(x, "moves left, but shouldn't be")


if __name__ == '__main__':
    unittest.main()
