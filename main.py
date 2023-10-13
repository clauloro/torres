from pilahanoi import Pila

def getTablero(n):
    pila1 = Pila()
    for i in range(n, 0, -1):
        pila1.push(i)
    return (pila1, Pila(), Pila())

def solve(tablero, disco, origen, destino, auxiliar):
    if disco == 1:
        movimiento = f"D{disco} from T{origen} to T{destino}"
        print(movimiento)
        tablero[destino - 1].push(tablero[origen - 1].pop())
    else:
        solve(tablero, disco-1, origen, auxiliar, destino)
        movimiento = f"D{disco} from T{origen} to T{destino}"
        print(movimiento)
        tablero[destino - 1].push(tablero[origen - 1].pop())
        solve(tablero, disco-1, auxiliar, destino, origen)

tablero = getTablero(5)
print("Contenido inicial de las pilas:")
print("Pila 1:", tablero[0])
print("Pila 2:", tablero[1])
print("Pila 3:", tablero[2])

print("\nLista de movimientos:")
solve(tablero, 5, 1, 3, 2)

print("\nContenido final de las pilas:")
print("Pila 1:", tablero[0])
print("Pila 2:", tablero[1])
print("Pila 3:", tablero[2])