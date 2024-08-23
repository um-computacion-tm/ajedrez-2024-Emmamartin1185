import unittest

class TestKing(unittest.TestCase):
    def test_white_king(self):
        white_king = King("WHITE")
        self.assertEqual(str(white_king), "♔")

    def test_black_king(self):
        black_king = King("BLACK")
        self.assertEqual(str(black_king), "♚")

if __name__ == '__main__':
    unittest.main()
 