# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:04:15 2026

@author: Luis Calle
"""

import pandas as pd
datos = pd.read_csv('ATP.csv')
print(datos.head())
datos.set_index('Location',inplace=True)
print('....................Melbourne...............')
print(datos.loc['Melbourne'])

print('....................Atlanta y Superficie............')
print(datos.loc['Atlanta','Surface'])