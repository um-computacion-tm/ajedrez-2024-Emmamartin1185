from ajedrez.chess import Chess

def main():
    chess = Chess()
    print_instructions()  # Mostrar las instrucciones del juego
    while chess.is_playing():
        play(chess)


def print_instructions():
    print("\n=== Bienvenido al Ajedrez ===")
    print("Para mover una pieza, ingresa las coordenadas de origen y destino.")
    print("Por ejemplo, para mover desde la fila 6, columna 4 a la fila 4, columna 4, ingresa:")
    print("From row: 6\nFrom col: 4\nTo row: 4\nTo col: 4\n")
    print("Recuerda que las filas y columnas van de 0 a 7 (como en un tablero de ajedrez).\n")
    print("¡Disfruta el juego!\n")


def play(chess):
    try:
        print(chess.show_board())  # Mostrar el tablero actual
        print("Turno de: ", "Blanco" if chess.turn == "WHITE" else "Negro")

        # Capturar las entradas del jugador
        from_row = int(input("Fila de origen: "))
        from_col = int(input("Columna de origen: "))
        to_row = int(input("Fila de destino: "))
        to_col = int(input("Columna de destino: "))

        # Validar las coordenadas
        if not validate_coordinates(from_row, from_col, to_row, to_col):
            print("Las coordenadas deben estar entre 0 y 7. Intenta de nuevo.\n")
            return

        # Intentar mover la pieza
        chess.move(from_row, from_col, to_row, to_col)

    except ValueError:
        print("Error: Ingresa números válidos para las coordenadas.\n")
    except Exception as e:
        print("Movimiento inválido:", e, "\n")


def validate_coordinates(from_row, from_col, to_row, to_col):
    """Verifica que las coordenadas estén dentro de los límites del tablero"""
    return all(0 <= x < 8 for x in [from_row, from_col, to_row, to_col])


if __name__ == "__main__":
    main()
