# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:08:42 2026

@author: Luis Calle
"""

import pandas as pd

import numpy as np

datos = {"Nombre":["Leo","Aldair","IngeDJ","Rodri","Jeferson"],
         "Calificaciones":["9","13","14","15","20"],
         "Deportes":["Ajedréz","Básquet","Natación","Fútbol","Balón mano"],
         "Materias":["Matemáticas","Métodos numéricos","Cocina","Educación Física","Física"]
         }

df = pd.DataFrame(datos)
print(df)

print("\n"*4)

datos2 = {"Nombre":["N/A","Aldair","IngeDJ","Rodri","Jeferson"],
         "Calificaciones":["9","13",np.nan,"15","20"],
         "Deportes":["N/A","Básquet","Natación","Fútbol","Balón mano"],
         "Materias":["Matemáticas","N/A","Cocina","Educación Física","Física"]
         }

df2 = pd.DataFrame(datos2)
print(df2)
print("\n"*4)
print(df2.info())
print("\n"*4)
print(df2.describe())
print("\n"*4)

nuevo = pd.DataFrame(df2)
nuevo = nuevo.replace(np.nan,"0")
print(nuevo)
print("\n"*4)
nuevo.info()
print("\n"*4)

nuevo2 = pd.DataFrame(df2)
nuevo2.dropna(how="any", inplace=True)
print(nuevo2)

print("\n"*4)
columna = df2[df2["Nombre"]!="NA"]

#2:25











