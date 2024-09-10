class ChessError(Exception):
    """Clase base para las excepciones relacionadas con el ajedrez."""
    pass

class InvalidMoveError(ChessError):
    """Excepción levantada cuando se intenta realizar un movimiento inválido."""
    def __init__(self, from_position, to_position, message="Movimiento inválido"):
        self.from_position = from_position
        self.to_position = to_position
        self.message = f"{message}: {from_position} -> {to_position}"
        super().__init__(self.message)
        
class PieceNotFoundError(ChessError):
    """Excepción levantada cuando no se encuentra una pieza en la posición especificada."""
    def __init__(self, position, message="No hay ninguna pieza en esta posición"):
        self.position = position
        self.message = f"{message}: {position}"
        super().__init__(self.message)

class InvalidPieceError(ChessError):
    """Excepción levantada cuando se intenta mover una pieza que no pertenece al jugador en turno."""
    def __init__(self, piece, message="Pieza no válida para mover"):
        self.piece = piece
        self.message = f"{message}: {piece}"
        super().__init__(self.message)