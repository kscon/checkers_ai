from core.Piece import Piece


class Field:
    col = ''
    row = ''
    piece = None

    def __init__(self, col, row):
        self.col = col
        self.row = row

    def set_Piece(self, piece: Piece):
        self.piece = piece

    def get_Piece(self):
        return self.piece

    def reset_Field(self):
        self.piece = None
