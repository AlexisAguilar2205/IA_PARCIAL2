
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:27:24 2023

@author: PC
"""

def counting_sort(arr):
    # Encuentra el valor máximo en la lista
    max_val = max(arr)
    
    # Inicializa una lista de conteo con ceros
    count = [0] * (max_val + 1)
    
    # Realiza el conteo de la frecuencia de cada elemento
    for num in arr:
        count[num] += 1
    
    # Reconstruye la lista ordenada
    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

# Ejemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)

print("Lista ordenada:")
for element in sorted_arr:
    print(element)