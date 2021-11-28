# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# Tamaño del dataset
data.shape

# Columnas del dataset
data.columns
data.info
data.info()

# Acceder a una columna
data.Sexo
data['Sexo']

# Agrupar por columnas
data.groupby('Sexo').size()

# Reemplazar
data.Sexo.replace('f' ,'F', inplace=True)
data.Sexo.replace('m' ,'M', inplace=True)

# Agrupar por valor
data.Estado.value_counts()

# Normalizar el estado
data.Estado.replace('leve' , 'Leve' , inplace = True)
data.Estado.replace('LEVE' , 'Leve' , inplace = True)

""" TALLER """






















