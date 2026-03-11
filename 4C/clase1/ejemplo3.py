import pandas as pd

datos = pd.read_csv("./clase1/notas_examen.csv")

cantidad_alumnos = datos["Alumno"].count()

promedios = [datos.iloc[i].drop('Alumno').mean() for i in range(cantidad_alumnos)]

indice_mas_alto = promedios.index(max(promedios))

print(datos["Alumno"][indice_mas_alto])

