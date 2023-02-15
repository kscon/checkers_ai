class Piece:
    player_color = ''  # white / black
    piece_type = ''  # pawn / queen

    def __init__(self, player_color, piece_type):
        self.player_color = player_color
        self.piece_type = piece_type

    def set_piece_type(self, piece_type):
        self.piece_type = piece_type

    def get_piece_type(self):
        return self.piece_type
