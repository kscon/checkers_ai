from core.GameDriver import GameDriver

gd = GameDriver()
gd.prepare_game()
lom = gd.ai.enumerate_moves()
print(lom)
gd.print_board()
