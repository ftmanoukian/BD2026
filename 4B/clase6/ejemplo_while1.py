"""
Pedirle al usuario que ingrese un número entero a través del terminal
"""

num_ingresado = input("Ingrese un número entero: ")

while not num_ingresado.isnumeric():
  print("No se ingresó un número entero")

  num_ingresado = input("Ingrese un número entero: ")