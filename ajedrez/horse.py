class Horse:
    def __init__(self, color):
        self.color = color

    def __str__(self):

        return "♘" if self.color == "WHITE" else "♞"

    def can_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento es válido para el caballo.
        El caballo se mueve en forma de 'L': dos casillas en una dirección (horizontal o vertical) 
        y luego una en perpendicular, o una casilla en una dirección y dos en perpendicular.
        """
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # Movimiento en 'L': 2 casillas en una dirección y 1 en la otra
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return self._is_valid_destination(to_row, to_col, board)

        return False

    def _is_valid_destination(self, to_row, to_col, board):
        """
        Verifica si la casilla de destino es válida (está vacía o contiene una pieza del oponente).
        """
        destination_piece = board[to_row][to_col]
        # Casilla vacía
        if destination_piece is None:
            return True
        # Hay una pieza del oponente en la casilla
        elif destination_piece.color != self.color:
            return True  # Captura válida
        return False  # No puede capturar una pieza del mismo color
    
    def test_horse_cannot_capture_ally():
     board = [[None] * 8 for _ in range(8)]
     horse = Horse("WHITE")
     ally_piece = Piece("WHITE")
     board[6][5] = ally_piece
    
    # Movimiento en 'L' pero no puede capturar una pieza aliada
    assert horse.can_move(4, 4, 6, 5, board) == False


    def test_horse_cannot_move_invalid():
        board = [[None] * 8 for _ in range(8)]
        horse = Horse("WHITE")
    
    # Movimiento inválido (no es en 'L')
    assert horse.can_move(4, 4, 4, 5, board) == False
    assert horse.can_move(4, 4, 5, 5, board) == False

 
