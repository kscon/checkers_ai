from Field import Field
from Piece import Piece


class Board:
    board = {}
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    board_size = 8

    def __init__(self):
        # self.init_board()
        pass

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

    # todo
    def board_to_string(self):
        s = ""
        for row in reversed(self.rows):
            for col in self.cols:
                piece = self.get_field(col,row).get_Piece()
                if piece is not None:
                    s+= '|' + piece.to_string()
                else:
                    s+= '| '
            s += '|\n'

        return s

    # todo
    # does NOT check for validity
    def move_piece(self, source_field, target_field):
        source_col, source_row = source_field
        target_col, target_row = target_field
        field = self.get_field(source_col, int(source_row))
        piece = field.get_Piece()
        field.set_Piece(' ')
        self.get_field(target_col, int(target_row)).set_Piece(piece)

    # todo
    def remove_piece(self, field):
        pass

    # todo
    def upgrade_piece(self, piece):
        pass

b = Board()
b.init_board()
b.init_pieces()
print(b.board_to_string())
# print(b.board_to_string())
# b.move_piece('A3','B4')
# print(b.board_to_string())