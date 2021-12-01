# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 10:30:00 2021

@author: Andrés Díaz
"""

import pandas as pd

"""
Tomando como base la información suministrada de casos de Covid-19 en
Colombia.
Realice las líneas de código en Python que den respuesta a las siguientes
preguntas:
"""

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

data['Nombre municipio'].replace(
    'puerto colombia', 'PUERTO COLOMBIA', inplace=True)

data['Nombre departamento'].replace('Tolima', 'TOLIMA', inplace=True)
data['Nombre departamento'].replace('Caldas', 'CALDAS', inplace=True)

data['Ubicación del caso'].replace('casa', 'Casa', inplace=True)
data['Ubicación del caso'].replace('CASA', 'Casa', inplace=True)

data.Sexo.replace('f', 'F', inplace=True)
data.Sexo.replace('m', 'M', inplace=True)
