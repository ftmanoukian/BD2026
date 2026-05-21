alumnos = []

while True:

  while True:
    nombre = input("Ingrese el nombre (o 'fin' para finalizar): ")
    if nombre.isalpha():
      break
    else:
      print("Ingrese un nómbre válido")

  if nombre == 'fin':
    break

  while True:
    nota_mate = input("Ingrese la nota de matemática: ")
    if nota_mate.isnumeric() and int(nota_mate) >= 0 and int(nota_mate) <= 10:
      nota_mate = int(nota_mate)
      break
    else:
      print("Ingrese una nota válida")
  
  while True:
    nota_lengua = input("Ingrese la nota de lengua: ")
    if nota_lengua.isnumeric() and int(nota_lengua) >= 0 and int(nota_lengua) <= 10:
      nota_lengua = int(nota_lengua)
      break
    else:
      print("Ingrese una nota válida")

  while True:
    nota_bd = input("Ingrese la nota de BD: ")
    if nota_bd.isnumeric() and int(nota_bd) >= 0 and int(nota_bd) <= 10:
      nota_bd = int(nota_bd)
      break
    else:
      print("Ingrese una nota válida")

  alumno = {"nombre":nombre, "nota mate":nota_mate, "nota lengua":nota_lengua, "nota bd":nota_bd}
  alumnos.append(alumno)

print("La cantidad total de alumnos es:", len(alumnos))

for alumno in alumnos:
  promedio = (alumno["nota mate"] + alumno["nota lengua"] + alumno["nota bd"]) / 3

  print(alumno["nombre"], "tiene promedio", promedio)