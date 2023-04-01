import unittest

from core.GameDriver import GameDriver
from core.Board import Board

# todo: automate testing
class GameDriverTestCase(unittest.TestCase):
    def test_move_validity_1(self):
        gd = GameDriver()
        # gd.print_board()
        self.assertTrue(gd.is_valid_move('a', 3, 'b', 4))
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
