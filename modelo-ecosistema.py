import random

class Presa:
    def __init__(self, animal_presa):
        self.animal_presa: str = animal_presa
        self.energia: int = 50

    def alimentarse(self):
        pass
    
    def __str__(self):
        return self.animal

class Depredador:
    def __init__(self, animal_depredador):
        self.animal_depredador: str = animal_depredador
        self.energia: int = 50
    
    def alimentarse(self):
        pass
    
    def __str__(self):
        return self.animal_depredador
    

def crear_matriz(n: int, i:int = 0, j:int = 0,  fila:list = [],matriz: list[list[int]] = []) -> list[list]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return crear_matriz(n, i + 1, 0, [], matriz)
    
    fila.append("_")
    return crear_matriz(n, i, j + 1, fila, matriz)

def agregar_elementos(matriz):
    limite = len(matriz) - 1
    print(matriz)
    i = random.randint(0, limite)
    j = random.randint(0, limite)

    if matriz[i][j] == "_":
        matriz[i][j] = "P"
    print("____________________"*3)
    print (matriz)

matriz = crear_matriz(3)
elementos = agregar_elementos(matriz)