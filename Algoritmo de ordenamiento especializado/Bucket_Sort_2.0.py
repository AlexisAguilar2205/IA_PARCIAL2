
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:40:03 2023

@author: PC
"""

def bucket_sort(arr):
    # Encuentra el valor máximo y mínimo en la lista
    max_val = max(arr)
    min_val = min(arr)

    # Establece el número de cubos (intervalos) y el tamaño de cada cubo
    num_buckets = 10  # Puedes ajustar esto según tus necesidades
    bucket_range = (max_val - min_val) / num_buckets

    # Crea los cubos
    buckets = [[] for _ in range(num_buckets + 1)]

    # Coloca los elementos en los cubos apropiados
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Ordena cada cubo (puedes usar otro algoritmo de ordenamiento)
    sorted_buckets = []
    for bucket in buckets:
        if bucket:
            insertion_sort(bucket)  # Ordena cada cubo usando Insertion Sort
            sorted_buckets.extend(bucket)

    return sorted_buckets

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bucket_sort(arr)

print("Lista ordenada:")
for element in sorted_arr:
    print(element)