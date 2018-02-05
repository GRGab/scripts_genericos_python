#!/usr/bin/env python



# Extraído de https://stackoverflow.com/questions/36834505/creating-a-spiral-array-in-python

N, S, O, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {N: E, E: S, S: O, O: N} # old -> new direction

def spiral(width, height):
    """Construye una matriz en la cual cada entrada indiza el paso
    en que fue visitada a lo largo de un camino en espiral"""
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # start near the center
    dx, dy = N # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))

   
#%%

# Ejemplo de uso de un generador
def foo():
    # Crea una lista infinita de enteros
	i = 0
	while 1:
		yield i
		i = i + 1

# Ahora uso foo() para iterar:
for x in foo():
    print(x)
    # Como es infinito, tengo que pararlo a mano:
    if x >= 13:
        break
#%%

"""Quiero armar un _generador_ que me dé el recorrido
espiralado en la grilla de NxN para cualquier
posición inicial"""

import numpy as np        

def camino_espiral(x_i, y_i):
    """Generador para iterar sobre un camino espiralado sobre una grilla de
    números enteros. Por conveniencia se pide que los valores iniciales sean
    positivos, pero el camino atraviesa coordenadas negativas también."""
    if x_i < 1 or y_i < 1:
        raise ValueError

    N, S, O, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
    turn_right = {N: E, E: S, S: O, O: N} # old -> new direction
    
    x, y = x_i, y_i
    dx, dy = N # initial direction
#    count = 0 #Por si quisiera seguir el número de pasos
    visitados = []
    while True:
#       count += 1
        yield (x, y)
        visitados.append((x,y))
        #try to turn right
        new_dx, new_dy = turn_right[(dx,dy)]
        new_x, new_y = x + new_dx, y + new_dy
        if (new_x, new_y) not in visitados: # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: #move straight
            x, y = x + dx, y + dy

#%%
# Ejemplo de utilización de lo que hemos creado
mapa = np.zeros((20,20), dtype=int)

i = 0
for (x,y) in camino_espiral(1,5):
    if x >= 1 and y >= 1:
        mapa[y-1,x-1] = i+1
        i += 1
    if i>= 90:
        break
#np.set_printoptions(threshold=np.inf)
print(mapa)



