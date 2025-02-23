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

class Planta:
    def __init__(self):
        self.planta: str = "P"
    
    def __repr__(self):
        return self.planta

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

ecosistema = crear_matriz(5)
depredador = agregar_depredadores(ecosistema)
presa = agregar_presas(ecosistema)
planta = agregar_planta(ecosistema)
print(ecosistema)