import random

class Presa:
    def __init__(self, animal_presa):
        self.animal_presa: str = animal_presa

    def alimentarse(self):
        pass
    
    def __repr__(self):
        return self.animal_presa

class Depredador:
    def __init__(self, animal_depredador):
        self.animal_depredador: str = animal_depredador
        self.energia: int = 50
    
    def alimentarse(self):
        pass
    
    def __reper__(self):
        return self.animal_depredador
    

def crear_matriz(n: int, i:int = 0, j:int = 0,  fila:list = [],matriz: list[list[int]] = []) -> list[list]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return crear_matriz(n, i + 1, 0, [], matriz)
    
    fila.append("_")
    return crear_matriz(n, i, j + 1, fila, matriz)

def agregar_al_ecosistema(matriz: list, cont: int =0):
    limite = len(matriz) - 1
    i = random.randint(0, limite)
    j = random.randint(0, limite)
    if cont > len(matriz):
        return matriz
    
    if matriz[i][j] == "_":
        matriz[i][j] = "P"
    
    if matriz[i][j] == "P":
        pass

    return agregar_presas(matriz, cont + 1)

def agregar_presas(matriz: list, cont_presas: int = 0):
    limite = len(matriz) - 1
    i = random.randint(0, limite)
    j = random.randint(0, limite)
    if cont_presas == len(matriz):
        return matriz
    if matriz[i][j] == "_":
        matriz[i][j] = "P"

    if matriz[i][j] == "P":
        pass
    return agregar_presas(matriz, cont_presas + 1)

def agregar_depredadores(matriz: list, cont_depredadores: int = 0):
    limite = len(matriz) - 1
    i = random.randint(0, limite)
    j = random.randint(0, limite)
    if cont_depredadores == len(matriz):
        return matriz
    if matriz[i][j] == "P" or "D":
        pass
    
    if matriz[i][j] == "_":
        matriz[i][j] = "D"
    
    return agregar_depredadores(matriz, cont_depredadores+1)

ecosistema = crear_matriz(3)
depredador = agregar_depredadores(ecosistema)
presa = agregar_presas(ecosistema)

print(ecosistema)