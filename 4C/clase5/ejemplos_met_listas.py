pizza = ['alcaucil','napo','cebolla','j&m','muzza','cancha','peppe','anchoas']

porcion_removida = pizza.pop(pizza.index('anchoas'))
pizza.sort()

print("La porción que sacamos es:",porcion_removida)
print("La pizzá quedó así:", pizza)
