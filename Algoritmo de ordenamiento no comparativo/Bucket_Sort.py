
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:39:31 2023

@author: PC
"""

def bucket_sort(arr):
    # Encuentra el valor máximo y mínimo en la lista
    max_val = max(arr)
    min_val = min(arr)
    
    # Crea las cubetas vacías
    num_buckets = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribuye los elementos en las cubetas
    for num in arr:
        index = num - min_val
        buckets[index].append(num)
    
    # Ordena cada cubeta (puedes usar otro algoritmo de ordenamiento)
    sorted_buckets = []
    for bucket in buckets:
        if bucket:
            sorted_bucket = sorted(bucket)
            sorted_buckets.extend(sorted_bucket)
    
    return sorted_buckets

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bucket_sort(arr)

print("Lista ordenada:")
for element in sorted_arr:
    print(element)