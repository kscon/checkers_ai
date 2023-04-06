from core.GameDriver import GameDriver

gd = GameDriver()
lom = gd.ai.enumerate_moves(gd.game_board)
print(lom)