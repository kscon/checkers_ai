class Field:
    col = ''
    row = ''
    piece = ' '

    def __init__(self, col, row):
        self.col = col
        self.row = row

    def set_Piece(self, piece_symbol):
        self.piece = piece_symbol

    def get_Piece(self):
        return self.piece
