# Creación de una tupla
mi_gran_tupla = ("Hola", "Cómo", "Estás", "Cómo")

# Encontramos la primera aparición de "Cómo"
ind_1 = mi_gran_tupla.index("Cómo")

print(ind_1)

# Encontramos la segunda aparición de "Cómo"
ind_2 = mi_gran_tupla.index("Cómo", ind_1 + 1)

print(ind_2)