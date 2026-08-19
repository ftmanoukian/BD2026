from tateti_lib import jugar_tateti

while True:
  nombre_usuario  = input("Ingresá tu nombre: ").strip()
  dificultad      = input("Ingresá el nivel de dificultad deseado ('alto'/'medio'/'bajo'): ")
  inicial         = input("Ingresá qué jugador debe arrancar ('jugador'/'maquina'/'aleatorio'): ")

  jugar_tateti(nombre_usuario, dificultad, inicial)

  continuar = input("Presioná 'x' y enter para finalizar, o cualquier cosa para continuar: ")
  if continuar.lower() == 'x':
    break