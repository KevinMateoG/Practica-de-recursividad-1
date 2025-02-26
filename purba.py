import random

DIRECCIONES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movimientos ortogonales

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

class Planta:
    def __init__(self):
        self.planta: str = "P"
    
    def __repr__(self):
        return self.planta

def crear_ecosistema(n: int, i:int = 0, j:int = 0,  fila:list = [],matriz: list[list[int]] = []) -> list[list]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return crear_ecosistema(n, i + 1, 0, [], matriz)
    
    fila.append("_")
    return crear_ecosistema(n, i, j + 1, fila, matriz)

def buscar_presa(matriz, i, j, indice=0, presas=None):
    if presas is None:
        presas = []
    if indice == len(matriz):
        return presas[0] if presas else None
    if type(matriz[i][indice]) == type(Presa()):
        presas.append((i, indice))
    if type(matriz[indice][j]) == type(Presa()):
        presas.append((indice, j))
    return buscar_presa(matriz, i, j, indice + 1, presas)

def mover(matriz, i, j, ni, nj): #ni == nuevai, nj == nuevaj
    matriz[i][j], matriz[ni][nj] = '_', Depredador()
    return matriz

def mover_depredador(matriz, i, j):
    presa = buscar_presa(matriz, i, j)
    if presa:
        return mover(matriz, i, j, *presa)
    random.shuffle(DIRECCIONES)  # Aleatorizar movimientos
    for di, dj in DIRECCIONES:
        nueva_i, nueva_j = i + di, j + dj
        if 0 <= nueva_i < len(matriz) and 0 <= nueva_j < len(matriz) and matriz[nueva_i][nueva_j] == '_':
            return mover(matriz, i, j, nueva_i, nueva_j)
    return matriz

def mover_todos(matriz, i=0, j=0):
    if i == len(matriz):
        return matriz
    if j == len(matriz[i]):
        return mover_todos(matriz, i + 1, 0)
    return mover_todos(mover_depredador(matriz, i, j) if type(matriz[i][j]) == type(Depredador()) else matriz, i, j + 1)

def ejecutar_ciclo(matriz, dia=1, max_dias=None):
    if max_dias is None:
        max_dias = random.randint(3, 20)
    if dia > max_dias:
        return
    print(f"\nDía {dia}:")
    print(matriz)
    ejecutar_ciclo(mover_todos(matriz), dia + 1, max_dias)

def agregar_presas(matriz: list, cont_presas: int = 0):
    limite = len(matriz) - 1
    i = random.randint(0, limite)
    j = random.randint(0, limite)
    posiciones_libres = buscarga_libres(matriz)
    if cont_presas == len(matriz):
        return matriz

    if (i,j) in posiciones_libres:
        matriz[i][j] = Presa()
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
        matriz[i][j] = Depredador()
        return agregar_depredadores(matriz, cont_depredadores+1)
    
    return agregar_depredadores(matriz, cont_depredadores)

def agregar_planta(matriz: list, cont_planta: int = 0):
    limite = len(matriz) - 1
    i = random.randint(0, limite)
    j = random.randint(0, limite)
    posiciones_libres = buscarga_libres(matriz)
    if cont_planta == len(matriz):
        return matriz
    if (i,j) in posiciones_libres:
        matriz[i][j] = Planta()
        return agregar_planta(matriz, cont_planta+1)
    
    return agregar_planta(matriz, cont_planta)

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

# Inicialización del ecosistema
ecosistema = crear_ecosistema(4)
depredador = agregar_depredadores(ecosistema)
presa = agregar_presas(ecosistema)
planta = agregar_planta(ecosistema)

# Ejecutar la simulación
ejecutar_ciclo(ecosistema)