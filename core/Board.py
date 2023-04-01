from core.Field import Field
from core.Piece import Piece


class Board:
    board = {}
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        # self.init_board()
        self.init_board()
        self.init_pieces()

    def init_board(self):
        for col in self.cols:
            for row in self.rows:
                self.board[(col, row)] = Field(col, row)

    #
    def init_pieces(self):
        # white pieces
        for row in [1, 3]:
            for col in ['a', 'c', 'e', 'g']:
                self.get_field(col, row).set_Piece(Piece('white', 'pawn'))
        for col in ['b', 'd', 'f', 'h']:
            self.get_field(col, 2).set_Piece(Piece('white', 'pawn'))

        # black pieces
        for row in [6, 8]:
            for col in ['b', 'd', 'f', 'h']:
                self.get_field(col, row).set_Piece(Piece('black', 'pawn'))
        for col in ['a', 'c', 'e', 'g']:
            self.get_field(col, 7).set_Piece(Piece('black', 'pawn'))

    def get_field(self, col, row):
        return self.board[(col, row)]

    def get_field_by_index(self, col_index, row_index):
        return self.board[(self.cols[col_index], self.rows[row_index])]

    def board_to_string(self):
        s = ""
        for row in reversed(self.rows):
            for col in self.cols:
                piece = self.get_field(col, row).get_Piece()
                if piece is not None:
                    s += '|' + piece.to_string()
                else:
                    s += '| '
            s += '|\n'

        return s

    # does NOT check for validity
    # expects sanitized input
    def move_piece(self, source_col, source_row, target_col, target_row):
        source_field = self.get_field(source_col, source_row)
        target_field = self.get_field(target_col, target_row)
        piece = source_field.get_Piece()
        target_field.set_Piece(piece)
        source_field.reset_Field()

    # does NOT check for validity
    # expects sanitized input
    def remove_piece(self, target_col, target_row):
        target_field = self.get_field(target_col, target_row)
        target_field.reset_Field()

    def is_valid_move(self, current_player, source_col, source_row, target_col, target_row):
        piece = self.get_field(source_col, source_row).get_Piece()
        col_index_source = self.cols.index(source_col)
        row_index_source = self.rows.index(source_row)
        col_index_target = self.cols.index(target_col)
        row_index_target = self.rows.index(target_row)
        checked_field = ' '

        play_direction = 1  # 1 for white, -1 for black
        if current_player == 1:
            play_direction = -1

        # pawn moves
        if piece.get_piece_type() == 'pawn':
            # normal moves
            if abs(col_index_source - col_index_target) == 1:
                target_field = self.get_field(target_col, target_row)
                if target_row - source_row == play_direction and target_field.get_Piece() is None:
                    return 1, None
                """# normal move white
                if target_row - source_row == 1 and current_player == 0 and target_piece is None:
                    return 1
                # normal move black
                elif target_row - source_row == -1 and current_player == 1 and target_piece == ' ':
                    return 1"""

            # checking moves
            elif abs(col_index_source - col_index_target) == 2:
                # checking move left forward
                target_field = self.get_field(target_col, target_row)
                if target_row - source_row == 2 * play_direction and \
                        target_field.get_Piece() is None:
                    checked_field = self.get_field_by_index(
                        col_index_source + (col_index_target - col_index_source) - 1,
                        row_index_source + play_direction)
                    if checked_field.get_Piece() is None:
                        return -1, None
                    if checked_field.get_Piece().player_color == 'white' and current_player == 1:
                        return 1, checked_field
                    elif checked_field.get_Piece().player_color == 'black' and current_player == 0:
                        return 1, checked_field
            """# checking move left backwards
                        elif target_row - source_row == -2:
                            checked_piece = self.game_board.get_field(
                                self.game_board.cols[col_index_source + 1], source_row - 1).get_piece()
                            if checked_piece == 'b' or checked_piece == 'B':
                                return True
                        # checking move right
                        elif self.game_board.cols.index(source_col) - self.game_board.cols.index(target_col) == 2:
                            # checking move right forward
                            if target_row - source_row == 2:
                                checked_piece = self.game_board.get_field(
                                    self.game_board.cols[col_index_source - 1], source_row + 1).get_piece()
                                if checked_piece == 'b' or checked_piece == 'B':
                                    return True
                            # checking move right backwards
                            elif target_row - source_row == -2:
                                checked_piece = self.game_board.get_field(
                                    self.game_board.cols[col_index_source - 1], source_row - 1).get_piece()
                                if checked_piece == 'b' or checked_piece == 'B':
                                    return True"""
            # move not valid
        return -1, None


"""b = Board()
b.init_board()
b.init_pieces()
print(b.board_to_string())
b.move_piece('a', 3, 'b', 4)
print(b.board_to_string())"""
# print(b.board_to_string())
# b.move_piece('A3','B4')
# print(b.board_to_string())
