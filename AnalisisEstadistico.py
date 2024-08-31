#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:44:13 2024

@author: deivit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, pearsonr

# Cargar los datos desde un archivo CSV
data = pd.read_csv('archivo_limpio.csv')

# Mostrar las primeras filas del dataframe para verificar su estructura
print("Datos iniciales:")
print(data.head())
print(data['edad'].unique())  # Muestra los valores únicos en la columna de edad
print(data['hrs_internet'].unique()) 

# Cálculo de Medidas de Tendencia Central
media_edad = data['edad'].mean()
media_hrs_internet = data['hrs_internet'].mean()

moda_edad = data['edad'].mode()[0]
moda_hrs_internet = data['hrs_internet'].mode()[0]

# Cálculo de Medidas de Dispersión
varianza_edad = data['edad'].var()
varianza_hrs_internet = data['hrs_internet'].var()

desv_std_edad = data['edad'].std()
desv_std_hrs_internet = data['hrs_internet'].std()

# Cálculo de Medidas de Forma
sesgo_edad = skew(data['edad'])
sesgo_hrs_internet = skew(data['hrs_internet'])

curtosis_edad = kurtosis(data['edad'])
curtosis_hrs_internet = kurtosis(data['hrs_internet'])

# Cálculo de Medidas de Posición
min_edad = data['edad'].min()
min_hrs_internet = data['hrs_internet'].min()

cuartil2_edad = data['edad'].quantile(0.5)
cuartil2_hrs_internet = data['hrs_internet'].quantile(0.5)

decil3_edad = data['edad'].quantile(0.3)
decil3_hrs_internet = data['hrs_internet'].quantile(0.3)

print(f"\nMedidas de Tendencia Central y Dispersión:")
print(f"Media (Edad): {media_edad:.2f}")
print(f"Media (Horas de uso de Internet): {media_hrs_internet:.2f}")
print(f"Moda (Edad): {moda_edad}")
print(f"Moda (Horas de uso de Internet): {moda_hrs_internet}")
print(f"Varianza (Edad): {varianza_edad:.2f}")
print(f"Varianza (Horas de uso de Internet): {varianza_hrs_internet:.2f}")
print(f"Desviación Estándar (Edad): {desv_std_edad:.2f}")
print(f"Desviación Estándar (Horas de uso de Internet): {desv_std_hrs_internet:.2f}")
print(f"\nMedidas de Forma y Posición:")
print(f"Sesgo (Edad): {sesgo_edad:.2f}")
print(f"Sesgo (Horas de uso de Internet): {sesgo_hrs_internet:.2f}")
print(f"Curtosis (Edad): {curtosis_edad:.2f}")
print(f"Curtosis (Horas de uso de Internet): {curtosis_hrs_internet:.2f}")
print(f"Mínimo (Edad): {min_edad}")
print(f"Mínimo (Horas de uso de Internet): {min_hrs_internet}")
print(f"Cuartil 2 - Mediana (Edad): {cuartil2_edad:.2f}")
print(f"Cuartil 2 - Mediana (Horas de uso de Internet): {cuartil2_hrs_internet:.2f}")
print(f"Decil 3 (Edad): {decil3_edad:.2f}")
print(f"Decil 3 (Horas de uso de Internet): {decil3_hrs_internet:.2f}")

# Gráficas básicas

# Cálculo de límites y número de clases para la edad
min_edades = data['edad'].min()
max_edades = data['edad'].max()
num_clases_edad = int(np.ceil(np.log2(len(data['edad'])) + 1))  # Regla de Sturges

# Histograma de la edad
plt.figure(figsize=(10, 6))
sns.histplot(data['edad'], bins=range(min_edades, max_edades + 2), kde=True, color='blue', discrete=True)
plt.title('Distribución de las Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.xticks(range(min_edades, max_edades + 1))  # Asegúrate de mostrar solo los valores de edad enteros
plt.xlim(min_edades - 0.5, max_edades + 0.5)  # Ajusta los límites del eje x
plt.savefig('histograma_edades.png')  # Guardar la gráfica
plt.close()  # Cerrar la figura para liberar memoria

# Cálculo de límites y número de clases para horas de uso de Internet
min_horas = data['hrs_internet'].min()
max_horas = data['hrs_internet'].max()
num_clases_horas = int(np.ceil(np.log2(len(data['hrs_internet'])) + 1))  # Regla de Sturges

# Histograma de las horas de uso de Internet
plt.figure(figsize=(10, 6))
sns.histplot(data['hrs_internet'], bins=range(min_horas, max_horas + 2), kde=True, color='green', discrete=True)
plt.title('Distribución de las Horas de Uso de Internet')
plt.xlabel('Horas de Uso de Internet')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.xticks(range(min_horas, max_horas + 1))  # Asegúrate de mostrar solo los valores enteros
plt.xlim(min_horas - 0.5, max_horas + 0.5)  # Ajusta los límites del eje x
plt.savefig('histograma_horas_internet.png')  # Guardar la gráfica
plt.close()  # Cerrar la figura

# Diagrama de caja para Edad y Horas de uso de Internet
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, orient="h", palette="Set2")
plt.title('Diagrama de Caja para Edad y Horas de Uso de Internet')
plt.savefig('diagrama_caja.png')  # Guardar la gráfica
plt.close()  # Cerrar la figura

# Análisis adicional

# Detección de Outliers
print("\nDetección de Outliers usando IQR:")

# Edad
Q1_edad = data['edad'].quantile(0.25)
Q3_edad = data['edad'].quantile(0.75)
IQR_edad = Q3_edad - Q1_edad
outliers_edad = data[(data['edad'] < Q1_edad - 1.5 * IQR_edad) | (data['edad'] > Q3_edad + 1.5 * IQR_edad)]
print(f"Outliers en Edad:\n{outliers_edad}")

# Horas de uso de Internet
Q1_hrs_internet = data['hrs_internet'].quantile(0.25)
Q3_hrs_internet = data['hrs_internet'].quantile(0.75)
IQR_hrs_internet = Q3_hrs_internet - Q1_hrs_internet
outliers_hrs_internet = data[(data['hrs_internet'] < Q1_hrs_internet - 1.5 * IQR_hrs_internet) | (data['hrs_internet'] > Q3_hrs_internet + 1.5 * IQR_hrs_internet)]
print(f"Outliers en Horas de Uso de Internet:\n{outliers_hrs_internet}")

# Gráfico de dispersión y cálculo de correlación
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['edad'], y=data['hrs_internet'])
plt.title('Relación entre Edad y Horas de Uso de Internet')
plt.xlabel('Edad')
plt.ylabel('Horas de Uso de Internet')
plt.grid(True)
plt.savefig('grafico_dispercion.png')  # Guardar la gráfica
plt.close()  # Cerrar la figura

# Cálculo del coeficiente de correlación de Pearson
correlacion, p_valor = pearsonr(data['edad'], data['hrs_internet'])
print(f"\nCoeficiente de correlación de Pearson entre Edad y Horas de Uso de Internet: {correlacion:.2f}")
print(f"p-valor: {p_valor:.4f}")

# Interpretación de la correlación
if p_valor < 0.05:
    print("Existe una correlación estadísticamente significativa entre Edad y Horas de Uso de Internet.")
else:
    print("No existe una correlación estadísticamente significativa entre Edad y Horas de Uso de Internet.")

subset = data['edad'].sample(n=100, random_state=1)

