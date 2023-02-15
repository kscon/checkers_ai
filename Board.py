from field import Field


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
                self.get_field(col, row).set_Piece('w')
        for col in ['a', 'd', 'f', 'h']:
            self.get_field(col, 2).set_Piece('w')

        # white pieces
        for row in [6, 8]:
            for col in ['b', 'd', 'f', 'h']:
                self.get_field(col, row).set_Piece('b')
        for col in ['a', 'c', 'e', 'g']:
            self.get_field(col, 7).set_Piece('b')

    def get_field(self, col, row):
        return self.board[(col, row)]


    def board_to_string(self):
        s = ""
        for row in self.rows:
            for col in self.cols:
                s += '|' + self.get_field(col,row).get_Piece()
            s += '|\n'

        return s

    def move_piece(self, source_field, target_field):
        source_col, source_row = source_field
        target_col, target_row = target_field
        field = self.get_field_by_notation(source_col, int(source_row))
        piece = field.get_Piece()
        field.set_Piece(' ')
        self.get_field_by_notation(target_col, int(target_row)).set_Piece(piece)


b = Board()
b.init_board()
print(b.board_to_string())
# print(b.board_to_string())
# b.move_piece('A3','B4')
# print(b.board_to_string())
