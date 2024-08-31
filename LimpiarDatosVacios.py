#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:27:26 2024

@author: deivit
"""

import csv

# Nombre del archivo de entrada y salida
input_file = 'data.csv'
output_file = 'archivo_limpio.csv'

# Abrir el archivo de entrada y salida
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        # Eliminar columnas vacías
        cleaned_row = [field for field in row if field.strip()]

        # Verificar si la fila tiene datos
        if cleaned_row:  # Si hay algún valor en la fila
            writer.writerow(cleaned_row)

print(f"Limpieza completada. Se ha creado '{output_file}'.")
