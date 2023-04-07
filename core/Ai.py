# from core.Board import Board


class Ai:
    color = 0  # white=0, black=1
    method = 'random'
    # gd = None
    game_board = None

    def __init__(self, color, game_board):
        # self.gd = gamedriver
        self.color = color
        self.game_board = game_board

    def get_move(self, board):
        self.game_board = board
        move = ''
        self.enumerate_moves()
        self.evaluate_moves()
        return move

    def enumerate_moves(self):
        list_of_moves = []  # in the fashion of = ['a3b4', 'c3b5', ...]
        play_direction = 1
        if self.color == 1:
            play_direction = -1

        for col in self.game_board.cols:
            for row in self.game_board.rows:
                field = self.game_board.get_field(col, row)
                if field.get_Piece() is not None:
                    piece = field.get_Piece()
                    if self.color == 0 and piece.player_color == 'white' or \
                            self.color == 1 and piece.player_color == 'black':
                        if piece.get_piece_type() == 'pawn':
                            # enumerate possible moves
                            for col_dif in [-1, 1]:
                                for row_dif in [1, 2]:
                                    target_col = chr(ord(col) - row_dif * col_dif)
                                    target_row = row + row_dif * play_direction
                                    # if 60 <= ord(target_col) <= 68 and 1 <= target_row <= 8:
                                    is_valid = self.game_board.try_move(self.color, col + str(row),
                                                                        target_col + str(target_row))
                                    if is_valid == 1:
                                        list_of_moves.append(col + str(row) + target_col + str(target_row))
                            """if ord(col) > 61:
                                target_col = chr(ord(col) - 1)
                                target_row = row + play_direction
                                list_of_moves.append(col + str(row) + target_col + str(target_row))
                            if ord(col) < 68:
                                target_col = chr(ord(col) - 1)
                                target_row = row + play_direction
                                list_of_moves.append(col + str(row) + target_col + str(target_row))
                            if ord(col) > 62:
                                target_col = chr(ord(col) - 2)
                                target_row = row + 2 * play_direction
                                list_of_moves.append(col + str(row) + target_col + str(target_row))
                            if ord(col) > 62:
                                target_col = chr(ord(col) - 2)
                                target_row = row + 2 * play_direction
                                list_of_moves.append(col + str(row) + target_col + str(target_row))"""
        return list_of_moves

    def evaluate_moves(self):
        pass
