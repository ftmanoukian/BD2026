import csv

alumnos = []

archivo = open('notas_curso.csv')

suma_promedios = 0

for alumno in csv.DictReader(archivo):
  nombre = alumno['nombre']

  try:
    matematica = float(alumno['matematica'])
  except:
    print("La nota de matemática de", nombre, "no es válida")
    continue
  
  try:
    lengua = float(alumno['lengua'])
  except:
    print("La nota de lengua de", nombre, "no es válida")
    continue
  
  try:
    bd = float(alumno['bd'])
  except:
    print("La nota de bd de", nombre, "no es válida")
    continue
  
  try:
    ti = float(alumno['ti'])
  except:
    print("La nota de ti de", nombre, "no es válida")
    continue

  promedio = (matematica + lengua + bd + ti) / 4
  if promedio >= 6:
    print("El alumno", alumno['nombre'], "está aprobado")
  elif promedio >= 5.5:
    print("El alumno", alumno['nombre'], "está aprobado de favor")
  else:
    print("El alumno", alumno['nombre'], "no está aprobado")
  print("promedio:", promedio)

  suma_promedios = suma_promedios + promedio

  alumnos.append(alumno)

try:
  promedio_curso = suma_promedios / len(alumnos)
  print("Promedio general:", promedio_curso)
except ZeroDivisionError:
  print("No hay alumnos para realizar promedio general")

# Si utilizáramos la alternativa de with open... as ...:, no necesitamos esto
archivo.close()