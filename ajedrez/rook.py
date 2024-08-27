class Rook:    #prueba de clase
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "♖" if self.color == "WHITE" else "♜"

    def can_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento es válido para la torre.
        """
        # Movimiento en la misma columna o en la misma fila
        if from_row == to_row or from_col == to_col:
            # Verifica si el camino está libre (no hay piezas entre la posición inicial y la final)
            if self.is_path_clear(from_row, from_col, to_row, to_col, board):
                return True
        return False

    def is_path_clear(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si no hay piezas en el camino para la torre.
        """
        if from_row == to_row:  # Movimiento horizontal
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if board[from_row][col] is not None:
                    return False
        elif from_col == to_col:  # Movimiento vertical
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if board[row][from_col] is not None:
                    return False
        return True
