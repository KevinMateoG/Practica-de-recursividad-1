import random

class Presa:
    def __init__(self):
        self.animal_presa: str = "C"
    
    def alimentarse(self):
        pass
    
    def __repr__(self):
        return self.animal_presa

class Depredador:
    def __init__(self):
        self.animal_depredador: str = "L"
        self.energia: int = 50
    
    def alimentarse(self):
        pass
    
    def __repr__(self):
        return self.animal_depredador


def crear_matriz(n: int, i:int = 0, j:int = 0,  fila:list = [],matriz: list[list[int]] = []) -> list[list]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return crear_matriz(n, i + 1, 0, [], matriz)
    
    fila.append("_")
    return crear_matriz(n, i, j + 1, fila, matriz)

def agregar_presas(matriz: list, cont_presas: int = 0):
    limite = len(matriz) - 1
    i = random.randint(0, limite)
    j = random.randint(0, limite)
    posiciones_libres = buscarga_libres(matriz)
    if cont_presas == len(matriz):
        return matriz

    if (i,j) in posiciones_libres:
        matriz[i][j] = "P"
        return agregar_presas(matriz, cont_presas+1)
    
    return agregar_presas(matriz, cont_presas)

def agregar_depredadores(matriz: list, cont_depredadores: int = 0):
    limite = len(matriz) - 1
    i = random.randint(0, limite)
    j = random.randint(0, limite)
    posiciones_libres = buscarga_libres(matriz)
    if cont_depredadores == len(matriz):
        return matriz
    
    if (i,j) in posiciones_libres:
        matriz[i][j] = "D"
        return agregar_depredadores(matriz, cont_depredadores+1)
    
    return agregar_depredadores(matriz, cont_depredadores)

def buscarga_libres(matriz, i: int = 0, j: int = 0, cont: int = 0) -> list[tuple]:
    lista = []
    limite = len(matriz) * len(matriz)
    if limite == cont:
        return lista
    
    if j == len(matriz):
        return buscarga_libres(matriz, i+1, 0, cont)
    
    if matriz[i][j] == "_":
        posicion = (i, j)
        lista.append(posicion)
    
    return lista + buscarga_libres(matriz, i, j+1,cont+1)

def mover_depredador(matriz: list[list[str]], i: int = 0, j: int = 0) -> list[list[str]]:
    # Caso base: si hemos recorrido toda la matriz, retornar la matriz actual
    if i == len(matriz):
        return matriz
    
    # Caso base: si hemos recorrido toda la fila, pasar a la siguiente fila
    if j == len(matriz[i]):
        return mover_depredador(matriz, i + 1, 0)
    
    # Si encontramos al depredador en la posición (i, j)
    if matriz[i][j] == "D":
        # Buscar presas en la misma fila o columna
        presa_pos = buscar_presa(matriz, i, j, i, j + 1)  # Buscar en la fila
        if not presa_pos:
            presa_pos = buscar_presa(matriz, i, j, i + 1, j)  # Buscar en la columna
        
        # Si hay una presa, mover al depredador hacia ella
        if presa_pos:
            presa_i, presa_j = presa_pos
            # Mover en la fila
            if presa_i == i:
                if presa_j < j:
                    matriz[i][j - 1] = "D"  # Mover a la izquierda
                else:
                    matriz[i][j + 1] = "D"  # Mover a la derecha
            # Mover en la columna
            elif presa_j == j:
                if presa_i < i:
                    matriz[i - 1][j] = "D"  # Mover hacia arriba
                else:
                    matriz[i + 1][j] = "D"  # Mover hacia abajo
            # Eliminar la presa
            matriz[presa_i][presa_j] = "_"
            # Limpiar la posición anterior del depredador
            matriz[i][j] = "_"
            return matriz
        else:
            # Si no hay presas, mover aleatoriamente en una dirección ortogonal
            direcciones = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]  # Arriba, abajo, izquierda, derecha
            direcciones_validas = [(x, y) for x, y in direcciones if 0 <= x < len(matriz) and 0 <= y < len(matriz[0]) and matriz[x][y] == "_"]
            if direcciones_validas:
                nueva_i, nueva_j = random.choice(direcciones_validas)
                matriz[nueva_i][nueva_j] = "D"
                matriz[i][j] = "_"
            return matriz
    
    # Continuar buscando al depredador en la siguiente posición
    return mover_depredador(matriz, i, j + 1)


def buscar_presa(matriz: list[list[str]], depredador_i: int, depredador_j: int, i: int, j: int) -> tuple[int, int] | None:
    # Caso base: si estamos fuera de los límites de la matriz, no hay presa
    if i < 0 or i >= len(matriz) or j < 0 or j >= len(matriz[0]):
        return None
    
    # Si encontramos una presa, retornar su posición
    if matriz[i][j] == "P":
        return (i, j)
    
    # Buscar en la fila (derecha o izquierda)
    if depredador_i == i:
        if j < depredador_j:
            return buscar_presa(matriz, depredador_i, depredador_j, i, j - 1)  # Buscar a la izquierda
        else:
            return buscar_presa(matriz, depredador_i, depredador_j, i, j + 1)  # Buscar a la derecha
    # Buscar en la columna (arriba o abajo)
    elif depredador_j == j:
        if i < depredador_i:
            return buscar_presa(matriz, depredador_i, depredador_j, i - 1, j)  # Buscar hacia arriba
        else:
            return buscar_presa(matriz, depredador_i, depredador_j, i + 1, j)  # Buscar hacia abajo
    return None


# Ejemplo de uso
ecosistema = crear_matriz(5)
ecosistema = agregar_depredadores(ecosistema)
ecosistema = agregar_presas(ecosistema)
print("Ecosistema inicial:")
for fila in ecosistema:
    print(fila)

ecosistema = mover_depredador(ecosistema)
print("\nEcosistema después de mover al depredador:")
for fila in ecosistema:
    print(fila)




"""ecosistema = crear_matriz(4)
print(buscarga_libres(ecosistema))
depredador = agregar_depredadores(ecosistema)
presa = agregar_presas(ecosistema)
print(ecosistema)
"""
