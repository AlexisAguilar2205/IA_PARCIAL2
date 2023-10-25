
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:25:37 2023

@author: PC
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento actual que se va a insertar en la parte ordenada
        j = i - 1  # Índice del último elemento en la parte ordenada

        # Mover elementos de la parte ordenada que son mayores que 'key'
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertar el elemento en su posición correcta
        arr[j + 1] = key

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)

print("Lista ordenada:")
for i in range(len(arr)):
    print(arr[i])