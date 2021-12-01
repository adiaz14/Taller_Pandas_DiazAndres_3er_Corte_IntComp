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

# 1. Número de casos de Contagiados en el País.

print(f'Número de casos de contagiados en el país: {data.shape[0]}')

# 2. Número de Municipios Afectados

numero_municipios_afectados = len(data['Nombre municipio'].value_counts())
print(f'Número de municipios afectados: {numero_municipios_afectados}')

# 3. Liste los municipios afectados (sin repetirlos)

nombre_municipios = data['Nombre municipio'].unique()
count = 0
print('Lista de municipios afectados (sin repeticiones)')
for municipio in nombre_municipios:
    count += 1
    print(f'#{count}. {municipio}')

# 4. Número de personas que se encuentran en atención en casa

data['Ubicación del caso'].value_counts()
casos_casa = data[data['Ubicación del caso'] == 'Casa'].shape[0]
print(f'Número de personas con atención en casa: {casos_casa}')

# 5.Número de personas que se encuentran recuperados

data['Recuperado'].value_counts()
personas_recuperadas = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'Número de personas recuperadas: {personas_recuperadas}')

# 6. Número de personas que ha fallecido

personas_fallecidas = data[data.Estado == 'Fallecido'].shape[0]
print(f'Número de personas fallecidas: {personas_fallecidas}')

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)

print('Listar de mayor a menor por tipo de caso (Importado, en estudio,'
      'Relacionado)')
data["Tipo de contagio"].value_counts()

# 8. Número de departamentos afectados
data['Nombre departamento'].value_counts()
numero_departamentos_afectados = len(
    data['Nombre departamento'].value_counts())
print(f'Número de departamentos afectados: {numero_departamentos_afectados}')

# 9. Liste los departamentos afectados(sin repetirlos)

nombre_departamentos = data['Nombre departamento'].unique()
count = 0
print('Lista de departamentos afectados (sin repeticiones)')
for departamento in nombre_departamentos:
    count += 1
    print(f'#{count}. {departamento}')

# 10. Ordene de mayor a menor por tipo de atención

data['Ubicación del caso'].value_counts()

print('Listar de mayor a menor por tipo de atención')
tipo_atencion = data[data['Ubicación del caso'] != 'Fallecido']
tipo_atencion.groupby(['Ubicación del caso']).size()

# 11.Liste de mayor a menor los 10 departamentos con mas casos de contagiados

print('Top 10 de departamentos con mayor casos de contagios')
data['Nombre departamento'].value_counts().head(10)

# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

print('Top 10 de departamentos con mayor casos de fallecidos')
fallecidos = data[data['Estado'] == 'Fallecido']
fallecidos.groupby(['Nombre departamento']).size(
).sort_values(ascending=False).head(10)

# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados

print('Top 10 de departamentos con mayor casos de recuperados')
recuperados = data[data['Recuperado'] == 'Recuperado']
recuperados.groupby(['Nombre departamento']).size(
).sort_values(ascending=False).head(10)

# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados

print('Top 10 de municipios con mayor casos de contagios')
data['Nombre municipio'].value_counts().head(10)

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos

print('Top 10 de municipios con mayor casos de fallecidos')
fallecidos = data[data['Estado'] == 'Fallecido']
fallecidos.groupby(['Nombre municipio']).size(
).sort_values(ascending=False).head(10)

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados

print('Top 10 de municipios con mayor casos de recuperados')
recuperados = data[data['Recuperado'] == 'Recuperado']
recuperados.groupby(['Nombre municipio']).size(
).sort_values(ascending=False).head(10)

# 17. Liste agrupado por departamento y en orden de Mayor a menor las ciudades
# con mas casos de contagiados

print('Lista agrupada de departamentos y ciudades con  mas contagios '
      '(mayor a menor)')
data.groupby('Nombre departamento')['Nombre municipio'].value_counts()

# 18. Número de Mujeres y hombres contagiados por ciudad por departamento

print('Número de Mujeres y hombres contagiados por ciudad por departamento')
data.groupby(['Sexo', 'Nombre departamento', 'Nombre municipio']).size()

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por ciudad
# por departamento

print('Promedio de edad de contagiados por hombre y mujeres por ciudad '
      'por departamento')
data.groupby(['Sexo', 'Nombre departamento', 'Nombre municipio'])[
    'Edad'].mean()

# 20. Liste de mayor a menor el número de contagiados por país de procedencia

print('Número de contagiados por país de procedencia (De mayor a menor)')
data['Nombre del país'].value_counts()

# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios

print('Fechas con mayor contagio (De mayor a menor)')
data['Fecha de notificación'].value_counts()

# 22. Diga cual es la tasa de mortalidad y recuperación que tiene toda
# Colombia

# Tasa mortalidad = 1000 *  No. personas fallecidas/No. personas contagiadas
# Tasa recuperación = 1000 * No. personas recuperadas/No. personas contagiadas

contagiados = data.shape[0]
fallecidos = data[data.Estado == 'Fallecido'].shape[0]
recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]
tasa_mortalidad = 0
tasa_recuperacion = 0

tasa_mortalidad = (fallecidos/contagiados) * 1000
tasa_recuperacion = (recuperados/contagiados) * 1000

print(f'Tasa de mortalidad en Colombia: {tasa_mortalidad}')
print(f'Tasa de recuperación en Colombia: {tasa_recuperacion}')

# 23. Liste la tasa de mortalidad y recuperación que tiene cada departamento

tasa_mortalidad_depart = (data[data['Recuperado'] == 'fallecido'].groupby(
    'Nombre departamento').size() / len(data)) * 100

tasa_recuperacion_depart = (data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre departamento').size() / len(data)) * 100

print(f'Lista de tasa de mortalidad por departamento: '
      f'{tasa_mortalidad_depart} \n')
print(f'Lista de tasa de recuperación por departamento: '
      f'{tasa_recuperacion_depart}')

# 24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad

tasa_mortalidad_municipio = (data[data['Recuperado'] == 'fallecido'].groupby(
    'Nombre municipio').size() / len(data)) * 100

tasa_recuper_municipio = (data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre municipio').size() / len(data)) * 100

print(f'Lista de tasa de mortalidad por ciudad: {tasa_mortalidad_municipio}')
print(f'\n Lista de tasa de recuperación por ciudad: {tasa_recuper_municipio}')

# 25. Liste por cada ciudad la cantidad de personas por atención

tipo_atencion = data[data['Ubicación del caso'] != 'Fallecido']

atencion_por_ciudad = tipo_atencion.groupby(
    ['Nombre municipio', 'Ubicación del caso']).size().sort_values()
print(f'Lista de ciudades y tipo de atención: {atencion_por_ciudad}')

# 26. Liste el promedio de edad por sexo por cada ciudad de contagiados

avg_edad_sexo_ciudad = data.groupby(['Nombre municipio', 'Sexo']).Edad.mean()
print(f'Lista de promedios de edad por sexo por cada ciudad de contagiados: '
      f'{avg_edad_sexo_ciudad}')

# 27. Grafique las curvas de contagio, muerte y recuperación de toda Colombia
# acumulados

print('Gráfico: curva de contagio')
curva_contagio = data.groupby(
    'Fecha de diagnóstico').size().sort_values().plot()

print('Gráfico: curva de fallecidos')
curva_fallecidos = data[data['Recuperado'] == 'fallecido'].groupby(
    'Fecha de diagnóstico').size().sort_values().plot()

print('Gráfico: curva de recuperados')
curva_recuperados = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Fecha de diagnóstico').size().sort_values().plot()

# 28. Grafique las curvas de contagio, muerte y recuperación de los 10
# departamentos con mas casos de contagiados acumulados

print('Gráfica: Curva de contagio en los 10 departamentos con mas casos')
contagios_top_10_dept = data.groupby('Nombre departamento').size(
).sort_values(ascending=False).head(10).plot()

print('Gráfica: Curva de fallecidos en los 10 departamentos con mas '
      'fallecidos')
fallecidos_top_10_dept = data[data['Recuperado'] == 'fallecido'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10).plot()

print('Gráfica: Curva de recuperados en los 10 departamentos con mas '
      'recuperados')
recuperados_top_10_dept = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10).plot()

# 29. Grafique las curvas de contagio, muerte y recuperación de las 10
# ciudades con mas casos de contagiados acumulados

print('Gráfica: Curva de contagio en los 10 ciudades con mas casos')
contagios_top_10_ciudad = data.groupby('Nombre municipio').size(
).sort_values(ascending=False).head(10).plot()

print('Gráfica: Curva de fallecidos en los 10 ciudades con mas fallecidos')
fallecidos_top_10_ciudad = data[data['Recuperado'] == 'fallecido'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10).plot()

print('Gráfica: Curva de recuperados en los 10 ciudades con mas recuperados')
recuperados_top_10_ciudad = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10).plot()

# 30.  Liste de mayor a menor la cantidad de fallecidos por edad en toda
# Colombia.

fallecidos_edad = data[data['Recuperado'] == 'fallecido'].groupby(
    'Edad').size().sort_values(ascending=False)
print(f'Fallecidos por edad (Mayor a menor): {fallecidos_edad}')

# 31. Liste el porcentaje de personas por atención de toda Colombia

porcentaje_atencion = ((data.groupby('Ubicación del caso').size().sort_values(
    ascending=False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending=False)).sum())) * 100
print(f'Lista de porcentajes por atencion en toda Colombia: '
      f'{porcentaje_atencion}')

# 32. Haga un gráfico de barras por atención de toda Colombia

print('Gráfica (Bar): Tipo de Atención en toda Colombia')
bar_atencion = data.groupby(
    'Ubicación del caso').size().sort_values().plot(kind='bar')
