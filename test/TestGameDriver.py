import unittest

from core.GameDriver import GameDriver
from core.Board import Board


# todo: automate testing
class GameDriverTestCase(unittest.TestCase):
    def test_move_validity_1(self):
        gd = GameDriver()
        # gd.print_board()
        self.assertTrue(is_valid_move(gd.game_board, gd.current_player, 'a', 3, 'b', 4))
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
