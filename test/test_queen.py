import unittest
from ajedrez.queen import Queen

class TestQueen(unittest.TestCase):
    def setUp(self):
        # Tablero vacío de 8x8 (None representa una casilla vacía)
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
    
    def test_queen_valid_move_vertical(self):
        queen = Queen("WHITE")
        # Movimiento válido en la misma columna (vertical)
        self.assertTrue(queen.can_move(0, 0, 5, 0, self.empty_board))

    def test_queen_valid_move_horizontal(self):
        queen = Queen("WHITE")
        # Movimiento válido en la misma fila (horizontal)
        self.assertTrue(queen.can_move(0, 0, 0, 5, self.empty_board))

    def test_queen_valid_move_diagonal(self):
        queen = Queen("WHITE")
        # Movimiento válido en diagonal
        self.assertTrue(queen.can_move(0, 0, 3, 3, self.empty_board))

    def test_queen_invalid_move(self):
        queen = Queen("WHITE")
        # Movimiento inválido (no es ni diagonal ni en línea recta)
        self.assertFalse(queen.can_move(0, 0, 3, 4, self.empty_board))

    def test_queen_path_blocked_straight(self):
        queen = Queen("WHITE")
        # Colocamos una pieza en el camino (movimiento vertical bloqueado)
        self.empty_board[2][0] = Queen("BLACK")
        self.assertFalse(queen.can_move(0, 0, 5, 0, self.empty_board))

    def test_queen_path_blocked_diagonal(self):
        queen = Queen("WHITE")
        # Colocamos una pieza en el camino (movimiento diagonal bloqueado)
        self.empty_board[2][2] = Queen("BLACK")
        self.assertFalse(queen.can_move(0, 0, 3, 3, self.empty_board))