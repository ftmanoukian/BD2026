"""
Solicitar nombres de una lista de cantidad desconocida
"""

lista_alumnos = []

while True:
  alumno = input("Ingrese el nombre del siguiente alumno (o 'fin' para terminar): ")

  if alumno == 'fin':
    break

  lista_alumnos.append(alumno)

print("La lista ingresada es:")
print(lista_alumnos)