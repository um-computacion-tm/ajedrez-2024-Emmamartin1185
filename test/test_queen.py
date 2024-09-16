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