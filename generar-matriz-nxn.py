'''
Se desea implementar un programa en Python que permita generar una matriz al azar de NxN números enteros entre 0 y 255 (incluido).
Dada una matriz de esas características, construya una función que permita hacer los siguiente:
    - Recibe una matriz de dos dimensiones como parámetro.
    - El algoritmo debe retornar los cuatro valores adyacentes en forma horizontal, vertical o diagonal (incluida diagonal invertida)
        que den como resultado el mayor valor multiplicado entre ellos (debe buscarlos dentro de la matriz).
    - Suba su código a la plataforma eFinis, Algoritmos (P), en la sección de Ejercicio (Laboratorio 3 Evaluado)

Por ejemplo, para la matriz de la figura 1, la función implementada debería poder ser llamada con buscar_numeros(M)y retornar una lista con los
valores [26,63,78,14], pues son los valores que, multiplicados, dan la mayor multiplicación.

'''

import random
import numpy as np
from functools import reduce


def MatrizAleatoria(n):
    # Inicializar la matriz
    matriz = np.zeros([n, n], dtype=int)

    for fila in range(n):
        for columna in range(n):
            elementos = int(random.randint(0, 255))  # Generar un número aleatorio entre 0 y 255
            matriz[fila][columna] = elementos

    return matriz

print("La matriz de de ser como minimo de 4x4")
matrizCreada = MatrizAleatoria(int(input("Ingrese el tamaño de la matriz NxN : ")))# Crear matriz de 5x5
mult = []
matriz_mult = []
print()
print("Matriz creada ...")
print()
for j in matrizCreada:
    print(j)

def matriz_volteada(matriz):
    matriz_volteada_final=[]
    for recorrer in matriz:
        matriz_volteada_final.append(recorrer[::-1].tolist())
        
    return np.vstack(matriz_volteada_final)

def buscar_numero():
    # print(matriz[fila][columna], end=" ")
    
    MultiplicacionVertical(matrizCreada)
    MultiplicacionHorizontal(matrizCreada)
    MultiplicacionDiagonalNormal(matrizCreada)
    MultiplicacionDiagonalInversa(matrizCreada)

    maximo = max(mult)
    pos_maximo = mult.index(max(mult[::-1]))
    pos_multiplos = matriz_mult[pos_maximo]
    print("--------------------")
    print("RESULTADO :")
    print()
    print(f'{maximo} Es la maxima multiplicacion y pertenece a los valores -> {pos_multiplos}')


# Recorrer la matriz verticalmente
def MultiplicacionVertical(matriz):
    print("----------")
    print("Multiplicacion Vertical")
    print("----------")
    
    for columna in range(len(matriz[0])):
        matriz_temp = []
        for fila in range(len(matriz)):
            # print(fila)
            if fila < len(matriz - 1):
                matriz_temp.append(matriz[fila][columna])
            # print(matriz[fila][columna])
            if len(matriz_temp) == len(matriz):
                
                i = 0
                while i < len(matriz_temp):
                    if len(matriz_temp[i:i + 4]) >= 4:
                        
                        matriz_mult.append(matriz_temp[i:i + 4])
                        mult.append(reduce(lambda x, y: x * y, matriz_temp[i:i + 4]))
                        
                        print(
                            f'{matriz_temp[i:i + 4]} : Multiplicacion -> {reduce(lambda x, y: x * y, matriz_temp[i:i + 4])}')
                        
                    i += 1
    


# Recorrer la matriz horizontalmente
def MultiplicacionHorizontal(matriz):
    
    print("----------")
    print("Multiplicacion Horizontal")
    print("----------")
    for fila in range(len(matriz[0])):
        matriz_temp = []
        for columna in range(len(matriz)):
            
            if fila < len(matriz - 1):
                matriz_temp.append(matriz[fila][columna])
            # print(matriz[fila][columna])
            if len(matriz_temp) == len(matriz):
                i = 0
                while i < len(matriz_temp):
                    if len(matriz_temp[i:i + 4]) >= 4:
                        
                        matriz_mult.append(matriz_temp[i:i + 4])
                        mult.append(reduce(lambda x, y: x * y, matriz_temp[i:i + 4]))
                        
                        print(
                            f'{matriz_temp[i:i + 4]} : Multiplicacion -> {reduce(lambda x, y: x * y, matriz_temp[i:i + 4])}')
                    i += 1

                  
# Recorrer la matriz diagonalmente

def MultiplicacionDiagonalNormal(matriz):

    print("----------")
    print("Multiplicacion Diagonal")
    print("----------")
    matriz_temp = []
    for columna in range(len(matriz[0])):
        for fila in range(len(matriz)):
            # print(columna)
            # agrega a matriz_temp los elementos de la diagonal
            if fila == columna:
                matriz_temp.append(matriz[fila][columna])
                #print(matriz_temp)

            if len(matriz_temp) == len(matriz):
                i = 0
                while i < len(matriz_temp):
                    if len(matriz_temp[i:i + 4]) >= 4:
                        
                        matriz_mult.append(matriz_temp[i:i + 4])
                        mult.append(reduce(lambda x, y: x * y, matriz_temp[i:i + 4]))
                        
                        print(
                            f'{matriz_temp[i:i + 4]} : Multiplicacion -> {reduce(lambda x, y: x * y, matriz_temp[i:i + 4])}')
                    i += 1

    
# Recorrer la matriz diagonalmente inversa
def MultiplicacionDiagonalInversa(matriz):
    
    print("----------")
    print("Multiplicacion Diagonal Invertida")
    print("----------")
    matriz=matriz_volteada(matriz)
    matriz_temp = []
    for fila in range(len(matriz[::-1])):
        for columna in range(len(matriz)):
            # print(columna)
            # agrega a matriz_temp los elementos de la diagonal invertida
            if fila == columna:
                matriz_temp.append(matriz[fila][columna])
                if len(matriz_temp) == len(matriz):
                    i = 0
                    while i < len(matriz_temp):
                        if len(matriz_temp[i:i + 4]) >= 4:
                            
                         matriz_mult.append(matriz_temp[i:i + 4])
                         mult.append(reduce(lambda x, y: x * y, matriz_temp[i:i + 4]))
                         
                         print(
                            f'{matriz_temp[i:i + 4]} : Multiplicacion -> {reduce(lambda x, y: x * y, matriz_temp[i:i + 4])}')
                        i += 1
    


print('------------------------------')
print('Inicio de la busqueda de la multiplicacion de los numeros con mayor multiplicacion')

buscar_numero()



