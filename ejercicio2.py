# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:32:47 2026

@author: Luis Calle
"""

import pandas as pd
datos = pd.read_csv('ATP.csv')
print(datos.info())
print("\n"*2)
print(datos.head())
print("\n"*2)
print(datos.iloc[0:5]) #para recorrer el indice
print("\n"*2)

#Regiones salteados
print(datos.iloc[[0,3,3,6,23]]) #para recorrer mediante su id

print("\n"*2)
#COlumnas
print(datos.iloc[:,0:3])
print("\n"*2)
print(datos.iloc[[0,3,6,24],[0,5,6]])
print("\n"*2)
print(datos.iloc[0:5,5:8])
