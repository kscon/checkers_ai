import pytest

from core.Field import *

@pytest.mark.parametrize('col, row, expected_col, expected_row',
                         [
                            ("a", "1", "a", "1"),
                            ("b", "2", "b", "2"),
                            ("c", "3", "c", "3")
                         ])
class TestField:
    piece = None
    field = None

    @pytest.fixture
    def set_up_test_field(self, col, row):
        self.piece = Piece("white", "pawn")
        self.field = Field(col, row)

    def test_Field(self,set_up_test_field,col, row, expected_col, expected_row):
        assert self.field.get_col() == expected_col
        assert self.field.get_row() == expected_row

    def test_set_Piece(self,set_up_test_field,col, row, expected_col, expected_row):
        self.field.set_Piece(self.piece)
        assert self.field.get_Piece() is self.piece

    def test_get_Piece(self,set_up_test_field,col, row, expected_col, expected_row):
        self.field.set_Piece(self.piece)
        self.field.reset_Field()
        assert self.field.get_Piece() is None

