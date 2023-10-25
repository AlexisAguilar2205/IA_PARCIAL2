
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:46:01 2023

@author: PC
"""

import heapq

# Función para fusionar dos archivos ordenados
def merge_files(file1, file2, output_file):
    heap = []
    
    # Leer el primer elemento de cada archivo y agregarlo a la heap
    value1 = file1.readline().strip()
    value2 = file2.readline().strip()
    
    if value1:
        heap.append((value1, file1))
    if value2:
        heap.append((value2, file2))
    
    # Fusionar los elementos de los archivos ordenadamente
    with open(output_file, 'w') as output:
        while heap:
            min_value, source_file = heapq.heappop(heap)
            output.write(min_value + '\n')
            
            next_value = source_file.readline().strip()
            if next_value:
                heapq.heappush(heap, (next_value, source_file))

# Función para dividir un archivo en múltiples archivos más pequeños
def split_file(input_file, chunk_size):
    files = []
    
    with open(input_file) as input:
        buffer = []
        counter = 0
        for line in input:
            buffer.append(line)
            counter += 1
            if counter >= chunk_size:
                buffer.sort()  # Ordenar el búfer en memoria
                with open(f'chunk_{len(files)}.txt', 'w') as output:
                    output.writelines(buffer)
                files.append(f'chunk_{len(files)}.txt')
                buffer = []
                counter = 0
        
        if buffer:
            buffer.sort()  # Ordenar el último búfer en memoria
            with open(f'chunk_{len(files)}.txt', 'w') as output:
                output.writelines(buffer)
            files.append(f'chunk_{len(files)}.txt')
    
    return files

# Función principal de ordenamiento polifásico
def polyphase_sort(input_file, output_file):
    chunk_size = 1000  # Tamaño de cada búfer
    num_chunks = 5  # Número de archivos a fusionar en cada paso
    
    # Dividir el archivo en búferes más pequeños
    files = split_file(input_file, chunk_size)
    
    while len(files) > 1:
        next_files = []
        for i in range(0, len(files), num_chunks):
            chunk_files = files[i:i + num_chunks]
            output_chunk = f'output_{len(files)}.txt'
            merge_files(chunk_files[0], chunk_files[1], output_chunk)
            if len(chunk_files) > 2:
                for j in range(2, len(chunk_files)):
                    merge_files(output_chunk, chunk_files[j], output_chunk)
            next_files.append(output_chunk)
        files = next_files
    
    # Renombrar el archivo final
    import shutil
    shutil.move(files[0], output_file)

# Ejemplo de uso
input_file = 'unsorted_data.txt'
output_file = 'sorted_data.txt'
polyphase_sort(input_file, output_file)