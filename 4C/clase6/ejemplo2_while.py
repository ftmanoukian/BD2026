"""
Bloque de código que se repite indefinidamente/para siempre
"""

lista_de_alumnos = []

while True:
  nombre = input("Ingrese el número del siguiente alumno (o 'fin' para terminar): ")

  if nombre == 'fin':
    print("Finalizó el ingreso")
    break

  lista_de_alumnos.append(nombre)

print(lista_de_alumnos)