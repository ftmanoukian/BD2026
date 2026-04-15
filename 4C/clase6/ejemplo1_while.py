"""
Solicitar al usuario que ingrese sí o sí un valor numérico
"""

edad = input("Ingrese su edad: ")

while not edad.isnumeric():
  edad = input("No es válido. Ingrese nuevamente su edad: ")

print("Su edad en 10 años será de", int(edad) + 10, "años")

