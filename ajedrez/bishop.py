class Bishop:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "♗" if self.color == "WHITE" else "♝"
    def can_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento es válido para el peón.
        """
        direction = -1 if self.color == "WHITE" else 1  # Blanco se mueve hacia arriba (-1), negro hacia abajo (+1)
        start_row = 6 if self.color == "WHITE" else 1    # Fila de inicio para el peón blanco o negro
        
        # Movimiento normal de una casilla hacia adelante
        if to_row == from_row + direction and from_col == to_col:
            # Verifica si la casilla de destino está vacía
            if board[to_row][to_col] is None:
                return True
        
        # Movimiento inicial de dos casillas hacia adelante
        if from_row == start_row and to_row == from_row + 2 * direction and from_col == to_col:
            # Verifica si ambas casillas en el camino están vacías
            if board[from_row + direction][from_col] is None and board[to_row][to_col] is None:
                return True

        # Captura en diagonal
        if to_row == from_row + direction and abs(to_col - from_col) == 1:
            # Verifica si hay una pieza del oponente en la casilla de destino
            destination_piece = board[to_row][to_col]
            if destination_piece is not None and destination_piece.color != self.color:
                return True

        return False
    def is_path_clear(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si no hay piezas en el camino para el alfil.
        """
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        
        row, col = from_row + row_step, from_col + col_step
        while row != to_row and col != to_col:
            if board[row][col] is not None:
                return False
            row += row_step
            col += col_step
        
        return True