# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:44:53 2023

@author: PC
"""

def comb_sort(arr):
    n = len(arr)
    gap = n  # Inicializa el espacio entre los elementos a la longitud de la lista
    shrink = 1.3  # Factor de contracción

    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        swapped = False
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
comb_sort(arr)

print("Lista ordenada:")
for element in arr:
    print(element)
