"""Tateti (tres en línea) para jugar por terminal."""

import random
import time

__all__ = ["jugar_tateti"]


def jugar_tateti(nombre_usuario, dificultad="medio", inicial="aleatorio"):
    """Ejecuta una única partida de tatetí contra la máquina.

    Args:
        nombre_usuario (str): Nombre del jugador humano.
        dificultad (str): "bajo", "medio" o "alto".
        inicial (str): "maquina", "usuario" o "aleatorio".

    Returns:
        dict: Resultado y configuración efectiva de la partida.
    """
    _validar_configuracion(nombre_usuario, dificultad, inicial)

    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_inicial = (
        random.choice(("maquina", "usuario"))
        if inicial == "aleatorio"
        else inicial
    )
    turno = jugador_inicial

    print(f"\nTateti - {nombre_usuario} (X) vs. Máquina (O)")
    print(f"Dificultad: {dificultad}")
    print(f"Comienza: {_nombre_jugador(jugador_inicial, nombre_usuario)}")
    _mostrar_tablero(tablero)

    while True:
        if turno == "usuario":
            fila, columna = _pedir_jugada_usuario(tablero, nombre_usuario)
            tablero[fila][columna] = "X"
        else:
            _mostrar_pensamiento_maquina()
            fila, columna = _elegir_jugada_maquina(tablero, dificultad)
            tablero[fila][columna] = "O"

        _mostrar_tablero(tablero)

        ficha = "X" if turno == "usuario" else "O"
        if _hay_ganador(tablero, ficha):
            print(
                f"\nGanó {_nombre_jugador(turno, nombre_usuario)}."
            )
            ganador = turno
            time.sleep(2)
            break

        if _tablero_lleno(tablero):
            print("\nEmpate.")
            ganador = "empate"
            time.sleep(2)
            break

        turno = "maquina" if turno == "usuario" else "usuario"

    return {
        "ganador": ganador,
        "usuario": nombre_usuario,
        "inicial": jugador_inicial,
        "dificultad": dificultad,
    }


def _validar_configuracion(nombre_usuario, dificultad, inicial):
    if not isinstance(nombre_usuario, str) or not nombre_usuario.strip():
        raise ValueError("nombre_usuario debe ser un str no vacío.")

    if dificultad not in ("bajo", "medio", "alto"):
        raise ValueError(
            'dificultad debe ser "bajo", "medio" o "alto".'
        )

    if inicial not in ("maquina", "usuario", "aleatorio"):
        raise ValueError(
            'inicial debe ser "maquina", "usuario" o "aleatorio".'
        )


def _mostrar_tablero(tablero):
    lineas = [
        "",
        "      1   2   3",
        "    +---+---+---+",
    ]

    for indice, fila in enumerate(tablero, start=1):
        lineas.append(
            f"  {indice} | " + " | ".join(fila) + " |"
        )
        lineas.append("    +---+---+---+")

    print("\n".join(lineas))


def _pedir_jugada_usuario(tablero, nombre_usuario):
    while True:
        try:
            entrada = input(
                f"\n{nombre_usuario}, ingresá fila y columna (1 a 3), "
                "separadas por espacio: "
            )
            partes = entrada.split()

            if len(partes) != 2:
                raise ValueError

            fila, columna = (int(valor) for valor in partes)

            if not (1 <= fila <= 3 and 1 <= columna <= 3):
                print("Las coordenadas deben estar entre 1 y 3.")
                continue

            fila -= 1
            columna -= 1

            if tablero[fila][columna] != " ":
                print("Esa casilla ya está ocupada.")
                continue

            return fila, columna

        except ValueError:
            print(
                "Entrada inválida. Ejemplo válido: 2 3 "
                "(fila 2, columna 3)."
            )


def _mostrar_pensamiento_maquina():
    """Simula unos segundos de pensamiento antes de la jugada de la máquina."""
    segundos = 1.5
    print("\nTurno de la máquina. Pensando", end="", flush=True)

    for _ in range(int(segundos * 5)):
        time.sleep(.2)
        print(".", end="", flush=True)

    print()


def _elegir_jugada_maquina(tablero, dificultad):
    libres = _casillas_libres(tablero)

    if dificultad in ("medio", "alto"):
        jugada_ganadora = _buscar_jugada_decisiva(tablero, "O")
        if jugada_ganadora is not None:
            return jugada_ganadora

    if dificultad == "alto":
        jugada_bloqueo = _buscar_jugada_decisiva(tablero, "X")
        if jugada_bloqueo is not None:
            return jugada_bloqueo

    return random.choice(libres)


def _buscar_jugada_decisiva(tablero, ficha):
    for fila, columna in _casillas_libres(tablero):
        tablero[fila][columna] = ficha

        if _hay_ganador(tablero, ficha):
            tablero[fila][columna] = " "
            return fila, columna

        tablero[fila][columna] = " "

    return None


def _casillas_libres(tablero):
    return [
        (fila, columna)
        for fila in range(3)
        for columna in range(3)
        if tablero[fila][columna] == " "
    ]


def _hay_ganador(tablero, ficha):
    lineas = []

    lineas.extend(tablero)

    for columna in range(3):
        lineas.append([tablero[fila][columna] for fila in range(3)])

    lineas.append([tablero[i][i] for i in range(3)])
    lineas.append([tablero[i][2 - i] for i in range(3)])

    return any(all(celda == ficha for celda in linea) for linea in lineas)


def _tablero_lleno(tablero):
    return not _casillas_libres(tablero)


def _nombre_jugador(jugador, nombre_usuario):
    return nombre_usuario if jugador == "usuario" else "la máquina"

if __name__ == "__main__":
    nombre = input("Ingresá tu nombre: ").strip()

    for dificultad in ("bajo", "medio", "alto"):
        jugar_tateti(
            nombre_usuario=nombre,
            dificultad=dificultad,
            inicial="aleatorio",
        )

