class Field:
    col = ''
    row = ''
    piece = ' '

    def __init__(self, col, row):
        self.col = col
        self.row = row

    def set_Piece(self, piece_Symbol):
        self.piece = piece_Symbol

    def get_Piece(self):
        return self.piece
