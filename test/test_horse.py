import unittest
from ajedrez.horse import Horse

class TestHorse(unittest.TestCase):
    def setUp(self):
        # Tablero vacío de 8x8 (None representa una casilla vacía)
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]

    def test_horse_representation(self):
        white_horse = Horse("WHITE")
        black_horse = Horse("BLACK")
        
        self.assertEqual(str(white_horse), "♘")
        self.assertEqual(str(black_horse), "♞")

    def test_horse_valid_move(self):
        horse = Horse("WHITE")
        # Movimiento válido en L
        self.assertTrue(horse.can_move(4, 4, 6, 5, self.empty_board))  # 2 hacia abajo, 1 a la derecha
        self.assertTrue(horse.can_move(4, 4, 6, 3, self.empty_board))  # 2 hacia abajo, 1 a la izquierda
        self.assertTrue(horse.can_move(4, 4, 5, 6, self.empty_board))  # 1 hacia abajo, 2 a la derecha
        self.assertTrue(horse.can_move(4, 4, 5, 2, self.empty_board))  # 1 hacia abajo, 2 a la izquierda
