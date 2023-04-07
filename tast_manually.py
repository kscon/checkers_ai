from core.GameDriver import GameDriver
from core.Piece import Piece

"""gd = GameDriver()
gd.prepare_game()
lom = gd.ai.enumerate_moves()
print(lom)
gd.print_board()
"""
# test for queen movement
gd = GameDriver(human_player_color=0)
gd.prepare_game()
gd.game_board.get_field('c', 3).set_Piece(Piece('white', 'pawn'))
gd.game_board.get_field('b', 6).set_Piece(Piece('white', 'pawn'))
gd.game_board.get_field('d', 4).set_Piece(Piece('black', 'queen'))
gd.print_board()
print(gd.ai.enumerate_moves())