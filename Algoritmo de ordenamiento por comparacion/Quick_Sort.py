
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:26:35 2023

@author: PC
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Una lista vacía o con un solo elemento ya está ordenada
    else:
        pivot = arr[0]  # Se elige el primer elemento como pivote
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)

print("Lista ordenada:")
for element in sorted_arr:
    print(element)