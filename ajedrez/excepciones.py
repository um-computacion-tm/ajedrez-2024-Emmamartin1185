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

class PathBlockedError(ChessError):
    """Excepción levantada cuando hay una pieza bloqueando el camino de movimiento."""
    def __init__(self, from_position, to_position, message="Camino bloqueado"):
        self.from_position = from_position
        self.to_position = to_position
        self.message = f"{message} entre {from_position} y {to_position}"
        super().__init__(self.message)

class SameColorCaptureError(ChessError):
    """Excepción levantada cuando se intenta capturar una pieza del mismo color."""
    def __init__(self, from_position, to_position, message="No puedes capturar una pieza del mismo color"):
        self.from_position = from_position
        self.to_position = to_position
        self.message = f"{message}: {from_position} -> {to_position}"
        super().__init__(self.message)

class CheckError(ChessError):
    """Excepción levantada cuando un movimiento pone al rey en jaque."""
    def __init__(self, message="Movimiento inválido: el rey está en jaque"):
        super().__init__(message)