import pytest

from core.Piece import *

@pytest.mark.parametrize('color, piece_type, expected_color, expected_type, expected_upgrade, expected_to_string',
                         [("white", "pawn", "white", "pawn","queen", "w"),
                        ("white", "queen", "white", "queen","queen", "W"),
                        ("black", "pawn", "black", "pawn","queen", "b"),
                        ("black", "queen", "black", "queen","queen", "B")])
class TestPiece:
    piece = None

    @pytest.fixture
    def set_up(self, color, piece_type):
        self.piece = Piece(color, piece_type)

    def test_piece_creation(self,set_up, color, piece_type,expected_color, expected_type, expected_upgrade, expected_to_string):
        assert self.piece.get_piece_type() is expected_type


    def test_upgrade_piece(self, set_up, color, piece_type,expected_color, expected_type, expected_upgrade, expected_to_string):
        self.piece.upgrade_piece()
        assert self.piece.get_piece_type() is expected_upgrade

    def test_to_string(self, set_up, color, piece_type,expected_color, expected_type, expected_upgrade, expected_to_string):
        assert self.piece.to_string() == expected_to_string
