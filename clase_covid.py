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

# Diga cuantas mujeres han fallecido en Colombia por covid-19
data[(data.Sexo == 'F') & (data.Estado == 'Fallecido')].shape[0]

# Diga cuantos hombres han fallecido en Colombia por covid-19
data[(data.Sexo == 'M') & (data.Estado == 'Fallecido')].shape[0]

data[(data.Estado == 'Fallecido')].groupby('Sexo').size()

# Cuantos fallecidos hay en Colombia
data[(data.Estado == 'Fallecido')].shape[0]

data.groupby(['Estado', 'Sexo']).size()
data.groupby(['Sexo', 'Estado']).size()

data.Estado.value_counts().plot.bar()
data.Sexo.value_counts().plot.bar()

data['Nombre municipio'].value_counts().head(5)

# Cuantas mujeres fallecieron en Barranquilla

data[(data.Sexo == 'F') & (data.Estado == 'Fallecido') & (data['Nombre municipio'] == 'BARRANQUILLA')].shape[0]

barranquilla = data[data['Nombre municipio'] == 'BARRANQUILLA']
barranquilla.groupby(['Sexo', 'Estado']).size()

barranquilla[barranquilla.Sexo == 'F'].Estado.value_counts().plot.bar()

barranquilla.Estado.value_counts().sort_values(ascending = False)

barranquilla.groupby(['Estado', 'Sexo']).size().plot.bar()


# Convertir tipo de variable

data['fecha reporte web'] = pd.to_datetime(data['fecha reporte web'])

data.groupby('fecha reporte web').size().cumsum().plot()
data.groupby('fecha reporte web').size().plot()
data.groupby('fecha reporte web').size()

# Barranquilla

barranquilla['fecha reporte web'] = pd.to_datetime(barranquilla['fecha reporte web'])

barranquilla.groupby('fecha reporte web').size().cumsum().plot()
barranquilla.groupby('fecha reporte web').size().plot()
barranquilla.groupby('fecha reporte web').size()

# Sin repetir
data['Nombre municipio'].value_counts()



































