import unittest
from ajedrez.rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        # Tablero vacío de 8x8 (None representa una casilla vacía)
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]

    def test_rook_valid_move_horizontal(self):
        rook = Rook("WHITE")
        # Movimiento válido en la misma fila (horizontal)
        self.assertTrue(rook.can_move(0, 0, 0, 5, self.empty_board))

    def test_rook_valid_move_vertical(self):
        rook = Rook("WHITE")
        # Movimiento válido en la misma columna (vertical)
        self.assertTrue(rook.can_move(0, 0, 5, 0, self.empty_board))

    def test_rook_invalid_move_diagonal(self):
        rook = Rook("WHITE")
        # Movimiento inválido en diagonal
        self.assertFalse(rook.can_move(0, 0, 5, 5, self.empty_board))

    def test_rook_path_blocked_horizontal(self):
        rook = Rook("WHITE")
        # Colocamos una pieza en el camino
        self.empty_board[0][3] = Rook("BLACK")
        # Intento de movimiento horizontal con una pieza bloqueando
        self.assertFalse(rook.can_move(0, 0, 0, 5, self.empty_board))

    def test_rook_path_blocked_vertical(self):
        rook = Rook("WHITE")
        # Colocamos una pieza en el camino
        self.empty_board[3][0] = Rook("BLACK")
        # Intento de movimiento vertical con una pieza bloqueando
        self.assertFalse(rook.can_move(0, 0, 5, 0, self.empty_board))

    def test_rook_path_clear(self):
        rook = Rook("WHITE")
        # Movimiento válido en línea recta (horizontal) sin piezas bloqueando
        self.assertTrue(rook.can_move(0, 0, 0, 7, self.empty_board))
    def test_rook_captures_opponent(self):
        rook = Rook("WHITE")
        # Colocamos una pieza del oponente en el destino
        self.empty_board[0][5] = Rook("BLACK")
        # La torre debe poder capturar la pieza negra
        self.assertTrue(rook.can_move(0, 0, 0, 5, self.empty_board))
    def test_rook_captures_opponent(self):
        rook = Rook("WHITE")
        self.empty_board[0][0] = rook
        # Colocamos una pieza del oponente en el destino
        self.empty_board[0][5] = Rook("BLACK")
        # La torre debe poder capturar la pieza negra
        self.assertTrue(rook.can_move(0, 0, 0, 5, self.empty_board))
    
    def test_rook_cannot_capture_own_piece(self):
        rook = Rook("WHITE")
        self.empty_board[0][0] = rook
        # Colocamos una pieza del mismo color en el destino
        self.empty_board[0][5] = Rook("WHITE")
        # La torre no debe poder capturar la pieza blanca
        self.assertFalse(rook.can_move(0, 0, 0, 5, self.empty_board))

    def test_rook_cannot_move_out_of_board(self):
        rook = Rook("WHITE")
        self.empty_board[0][0] = rook
        # Intento de movimiento fuera del tablero
        self.assertFalse(rook.can_move(0, 0, 0, 8, self.empty_board))
if __name__ == "__main__": 
    unittest.main()
