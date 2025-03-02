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

def crear_ecosistema(n: int, i:int = 0, j:int = 0,  fila:list = [],matriz: list[list[int]] = []) -> list[list]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return crear_ecosistema(n, i + 1, 0, [], matriz)
    
    fila.append("_")
    return crear_ecosistema(n, i, j + 1, fila, matriz)

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
    if cont_depredadores >= len(matriz)//2:
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


def mover_depredadores(matriz, i: int = 0, j: int = 0, n: int = 0):
    limite = len(matriz) * len(matriz)
    if limite == n:
        return 

    if j == len(matriz):
        return mover_depredadores(matriz, i+1, 0, n)

    if type(matriz[i][j]) == type(Depredador()):
        posiciones = buscarga_libres(matriz)
        l = random.randint(0, len(posiciones)-1)
        ni, nj = posiciones[l]
        guardar = matriz[i][j]
        matriz[i][j] = "_"
        matriz[ni][nj] = guardar
        return mover_depredadores(matriz, i, j, n)

    return mover_depredadores(matriz, i, j+1, n+1)

def mover_presa(matriz, i: int = 0, j: int = 0, n: int = 0):
    limite = len(matriz) * len(matriz)
    if limite == n:
        return 

    if j == len(matriz):
        return mover_presa(matriz, i+1, 0, n)

    if type(matriz[i][j]) == type(Presa()):
        posiciones = buscarga_libres(matriz)
        l = random.randint(0, len(posiciones)-1)
        ni, nj = posiciones[l]
        guardar = matriz[i][j]
        matriz[i][j] = "_"
        matriz[ni][nj] = guardar
        return mover_presa(matriz, i, j, n)

    return mover_presa(matriz, i, j+1, n+1)

def mostrar_matriz(matriz, n=0):
    if n == len(matriz):
        return
    print(matriz[n])
    return mostrar_matriz(matriz, n+1)

def paso_de_dias(n:int, ecosistema: list, dias = 1, cont_dias = 0):
    print(f"---------dia {dias}-----------")
    mover_depredadores(ecosistema)
    mover_presa(ecosistema)
    mostrar_matriz(ecosistema)
    #if cont_dias == 4:
    #    reproducir_plantas()
    #   return dias(n, ecosistema, dias+1, 0)
    if n == dias:
        return
    return paso_de_dias(n, ecosistema, dias+1, cont_dias+1)

def reproducir_plantas(matriz: list, i: int = 0, j: int = 0, n: int = 0, cont_p: int = 0):
    ...

ecosistema = crear_ecosistema(4)
ecosistema = agregar_depredadores(ecosistema)
ecosistema = agregar_presas(ecosistema)
ecosistema = agregar_planta(ecosistema)
mostrar_matriz(ecosistema)
paso_de_dias(8, ecosistema)