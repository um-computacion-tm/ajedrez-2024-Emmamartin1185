import unittest
from ajedrez.pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_pawn_representation(self):
        white_pawn = Pawn("WHITE")
        black_pawn = Pawn("BLACK")

        
        self.assertEqual(str(white_pawn), "♙")
        self.assertEqual(str(black_pawn), "♟")

if __name__ == "__main__":
    unittest.main()
