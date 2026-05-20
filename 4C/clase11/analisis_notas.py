import csv

with open('./datos.csv','r',encoding='utf-8') as archivo:
  lector = csv.DictReader(archivo,delimiter=',')

  alumnos = []
  promedio_general = 0
  for fila in lector:
    alumnos.append(fila)

    print(fila)

    promedio = (int(fila["matematica"]) + int(fila["lengua"]) + int(fila["bd"]) + int(fila["ti"])) / 4

    if promedio >= 6:
      print("Aprobado")
    else:
      print("Desaprobado")
    print(promedio)
    print()

    promedio_general = promedio + promedio_general

  promedio_general = promedio_general / len(alumnos)
  print("Promedio general:",promedio_general)