import unittest
from ajedrez.rook import Rook

def test_rook_valid_move():
    rook = Rook("WHITE")

    # Movimiento válido en la misma fila
    assert rook.is_valid_move(0, 0, 0, 5) is True
    # Movimiento válido en la misma columna
    assert rook.is_valid_move(0, 0, 5, 0) is True
    # Movimiento inválido en diagonal
    assert rook.is_valid_move(0, 0, 5, 5) is False

def test_rook_color():
    rook_black = Rook("BLACK")
    rook_white = Rook("WHITE")

    assert rook_black.color == "BLACK"
    assert rook_white.color == "WHITE" 

if __name__ == '__main__':
    unittest.main()
