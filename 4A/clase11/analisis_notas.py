import csv

archivo = open('alumnos.csv')
alumnos = []

for fila in csv.DictReader(archivo):
  alumnos.append(fila)

suma_promedios = 0

for alumno in alumnos:
  promedio = (int(alumno['matematica']) + int(alumno['lengua']) + int(alumno['bd']) + int(alumno['ti'])) / 4
  suma_promedios = suma_promedios + promedio

  if promedio >= 6:
    print("El alumno", alumno['nombre'] ,"está aprobado con promedio", promedio)
  else:
    print("El alumno", alumno['nombre'] ,"NO está aprobado con promedio", promedio)

promedio_total = suma_promedios / len(alumnos)
print("El promedio total es de", promedio_total)