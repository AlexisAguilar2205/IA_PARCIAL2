
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:45:12 2023

@author: PC
"""

def optimized_bubble_sort(arr):
    n = len(arr)
    swapped = True  # Bandera para verificar si se han realizado intercambios

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]  # Intercambia elementos
                swapped = True  # Se han realizado intercambios en esta pasada

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
optimized_bubble_sort(arr)

print("Lista ordenada:")
for element in arr:
    print(element)