import csv

alumnos = []

archivo = open('notas_curso.csv')

for fila in csv.DictReader(archivo):
  alumnos.append(fila)

suma_promedios = 0

for alumno in alumnos:
  matematica = float(alumno['matematica'])
  lengua     = float(alumno['lengua'])
  bd         = float(alumno['bd'])
  ti         = float(alumno['ti'])

  promedio = (matematica + lengua + bd + ti) / 4
  if promedio >= 6:
    print("El alumno", alumno['nombre'], "está aprobado")
  elif promedio >= 5.5:
    print("El alumno", alumno['nombre'], "está aprobado de favor")
  else:
    print("El alumno", alumno['nombre'], "no está aprobado")
  print("promedio:", promedio)

  suma_promedios = suma_promedios + promedio

promedio_curso = suma_promedios / len(alumnos)
print("Promedio general:", promedio_curso)

# Si utilizáramos la alternativa de with open... as ...:, no necesitamos esto
archivo.close()