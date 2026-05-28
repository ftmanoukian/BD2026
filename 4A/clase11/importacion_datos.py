import csv

alumnos = []

with open('alumnos.csv') as archivo:

  # Vamos a empezar a recorrer el archivo fila por fila
  # leyendo cada fila como un diccionario
  for fila in csv.DictReader(archivo):

    # Guardamos la fila en la lista de alumnos
    alumnos.append(fila)

  # Imprimimos la lista completa
  print(alumnos)