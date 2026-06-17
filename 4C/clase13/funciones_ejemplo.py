# Vamos a hacer una primera función que salude a una persona por su nombre

# Recibe parámetros? - SI: el nombre
# Devuelve algún valor? - NO

def saludar(nombre):
  print("Hola", nombre)

"""
saludar("Fran")
saludar("Messi")
saludar("Don Pepito")
saludar("Don Jose")
"""






#Vamos a hacer una función que sume dos números

# Recibe parámetros? - SI: dos, que son los números a sumar
# Devuelve parámetros? - SI: uno, el resultado de la suma

def suma(numero1,numero2):
  resultado = numero1 + numero2

  return resultado


"""
print(suma(3,8))
"""





#Vamos a hacer una función que solicita un nombre hasta que sea válido

# ¿cómo quiero que se vea?
#  nombre_alumno = solicitar_nombre()

# Toma parámetros? - NO! El input() va a solicitar desde adentro 
#   de esta función
# Devuelve algún valor? - SI: El nombre

def solicitar_nombre():
  nombre = input("Ingrese el nombre: ")
  
  while not nombre.isalpha():
    print("Nombre inválido")
    nombre = input("Ingrese el nombre: ")

  return nombre

print("Hola", solicitar_nombre())





















