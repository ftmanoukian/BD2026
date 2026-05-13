# Creo la lista donde voy a almacenar los datos
alumnos = []

# Inicio el bucle de solicitud de datos
while True:
  nombre = input("Nombre (o 'fin' para terminar): ")

  # Si se ingresó 'fin', salgo del bucle
  if nombre == "fin":
    break

  # Si el nombre tiene caracteres no alfabéticos, vuelvo a iniciar
  if not nombre.isalpha():
    print("El nombre debe estar compuesto únicamente por letras")
    continue

  # Solicito la nota de matemática
  while True:
    matematica = input("Nota de matemática: ")
    if matematica.isnumeric():
      matematica = int(matematica)
      if matematica <= 10 and matematica >= 0:
        break
      else:
        print("La nota debe estar entre 0 y 10")
    else:
      print("⚠ NO se ingresó un número válido")

  # Solicito la nota de lengua
  while True:
    lengua = input("Nota de lengua: ")
    if lengua.isnumeric():
      lengua = int(lengua)
      if lengua <= 10 and lengua >= 0:
        break
      else:
        print("La nota debe estar entre 0 y 10")
    else:
      print("⚠ NO se ingresó un número válido")

  # Solicito la nota de BD
  while True:
    bd = input("Nota de BD: ")
    if bd.isnumeric():
      bd = int(bd)
      if bd <= 10 and bd >= 0:
        break
      else:
        print("La nota debe estar entre 0 y 10")
    else:
      print("⚠ NO se ingresó un número válido")

	# Guardo los datos del alumno actual
  alumno = {"nombre":nombre, "matematica":matematica, "lengua":lengua, "bd":bd}
  alumnos.append(alumno)

print("La cantidad de alumnos es:",len(alumnos))

for alumno in alumnos:
  promedio = (alumno["matematica"] + alumno["lengua"] + alumno["bd"]) / 3

  print("Alumno", alumno["nombre"], "promedio:", promedio)