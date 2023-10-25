
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:45:35 2023

@author: PC
"""

def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True

    start = 0
    end = n - 1

    while (swapped == True):
        # Resetea la bandera en cada pasada
        swapped = False

        # Mueve el elemento más grande hacia la derecha, como en el Bubble Sort
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Si no hubo intercambios, la lista está ordenada
        if (swapped == False):
            break

        # Reduce la porción ordenada en la parte derecha
        end = end - 1

        # Mueve el elemento más pequeño hacia la izquierda
        for i in range(end - 1, start - 1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Aumenta la porción ordenada en la parte izquierda
        start = start + 1

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
cocktail_shaker_sort(arr)

print("Lista ordenada:")
for element in arr:
    print(element)