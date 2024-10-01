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
 
    def test_horse_invalid_move(self):
        horse = Horse("WHITE")
        # Movimientos inválidos (no en L)
        self.assertFalse(horse.can_move(4, 4, 4, 5, self.empty_board))  # Movimiento horizontal
        self.assertFalse(horse.can_move(4, 4, 5, 5, self.empty_board))  # Movimiento diagonal
        self.assertFalse(horse.can_move(4, 4, 3, 3, self.empty_board))  # Movimiento en otra dirección

    def test_horse_capture_opponent(self):
        horse = Horse("WHITE")
        # Colocamos una pieza del oponente en el destino
        self.empty_board[6][5] = Horse("BLACK")
        # El caballo debe poder capturar la pieza negra
        self.assertTrue(horse.can_move(4, 4, 6, 5, self.empty_board))