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



"""b = Board()
b.init_board()
b.init_pieces()
print(b.board_to_string())
b.move_piece('a', 3, 'b', 4)
print(b.board_to_string())"""
# print(b.board_to_string())
# b.move_piece('A3','B4')
# print(b.board_to_string())
