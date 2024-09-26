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
