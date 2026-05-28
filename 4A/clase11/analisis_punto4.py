import csv

archivo = open('alumnos.csv')
alumnos = []
suma_promedios = 0

for alumno in csv.DictReader(archivo):
  nombre = alumno['nombre']

  # Intento convertir la nota de forma forzada
  try:
    matematica = int(alumno['matematica'])

    if matematica < 0 or matematica > 10:
      # Fuerzo que el programa tenga un error, para que vaya al except
      raise

  except:
    print("El alumno", nombre, "tiene una nota de matemática inválida")

    # Salteo a la próxima ejecución del bucle
    continue

  # Intento convertir la nota de forma forzada
  try:
    lengua = int(alumno['lengua'])

    if lengua < 0 or lengua > 10:
      # Fuerzo que el programa tenga un error, para que vaya al except
      raise

  except:
    print("El alumno", nombre, "tiene una nota de lengua inválida")

    # Salteo a la próxima ejecución del bucle
    continue

  # Intento convertir la nota de forma forzada
  try:
    bd = int(alumno['bd'])

    if bd < 0 or bd > 10:
      # Fuerzo que el programa tenga un error, para que vaya al except
      raise

  except:
    print("El alumno", nombre, "tiene una nota de bd inválida")

    # Salteo a la próxima ejecución del bucle
    continue

  # Intento convertir la nota de forma forzada
  try:
    ti = int(alumno['ti'])

    if ti < 0 or ti > 10:
      # Fuerzo que el programa tenga un error, para que vaya al except
      raise

  except:
    print("El alumno", nombre, "tiene una nota de ti inválida")

    # Salteo a la próxima ejecución del bucle
    continue

  promedio = (matematica + lengua + bd + ti) / 4
  suma_promedios = suma_promedios + promedio

  if promedio >= 6:
    print("El alumno", nombre ,"está aprobado con promedio", promedio)
  else:
    print("El alumno", nombre ,"NO está aprobado con promedio", promedio)

  alumnos.append(alumno)

try:
  promedio_total = suma_promedios / len(alumnos)
  print("El promedio total es de", promedio_total)
except:
  print("Hubo un error al calcular el promedio")