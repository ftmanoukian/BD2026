"""
Este programa utiliza un juego de ta-te-tí ya programado en el archivo 'tateti_lib.py', 
que debe encontrarse en la misma carpeta en la que descargues que este archivo. 
El terminal desde el que se corra el script también debe estar situado en la misma carpeta.

Tu objetivo es, partiendo desde este ejemplo, agregar un scoreboard (tabla de puntajes)
PERSISTENTE! Es decir, no se debe perder al cerrar el programa.

La forma en que se muestra este scoreboard es libre: podés hacerlo tan sencillo o detallado
como quieras. Lo importante es que, cuando volvamos a correr el juego, se siga viendo igual
que antes de cerrarlo.

NO debés modificar tateti_lib.py, pero podés modificar este archivo libremente.

¡Manos a la obra!
"""

from tateti_lib import jugar_tateti

while True:
  nombre_usuario  = input("Ingresá tu nombre: ").strip()
  dificultad      = input("Ingresá el nivel de dificultad deseado ('alto'/'medio'/'bajo'): ")
  inicial         = input("Ingresá qué jugador debe arrancar ('jugador'/'maquina'/'aleatorio'): ")

  jugar_tateti(nombre_usuario, dificultad, inicial)

  # Acá tenemos que mostrar un scoreboard! ¿cómo lo hacemos?

  continuar = input("Presioná 'x' y enter para finalizar, o cualquier cosa para continuar: ")
  if continuar.lower() == 'x':
    break