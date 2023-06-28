# helper class for treelib

class BoardState:
    board = {}
    move_log = []  # 'a3b4', 'b6c5', ...
    current_player = 0
    checked_pieces = {}  # turn:(piece, field)
    turn = 0

    def __init__(self, board, move_log, current_player, checked_pieces, turn):
        self.board = board
        self.move_log = move_log
        self.current_player = current_player
        self.checked_pieces = checked_pieces
        self.turn = turn
