
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:48:35 2023
@author: PC
"""

def adaptive_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Mover elementos de arr[0..i-1] que son mayores que key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
adaptive_insertion_sort(arr)

print("Lista ordenada:")
for element in arr:
    print(element)