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