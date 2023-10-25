
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:15:42 2023

@author: PC
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos 'i' elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print("Lista ordenada:")
for i in range(len(arr)):
    print(arr[i])