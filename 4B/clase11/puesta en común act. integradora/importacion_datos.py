import csv

alumnos = []

archivo = open('notas_curso.csv')
#otra alternativa
# with open('notas_curso.csv') as archivo:

for fila in csv.DictReader(archivo):
  alumnos.append(fila)

print(alumnos)