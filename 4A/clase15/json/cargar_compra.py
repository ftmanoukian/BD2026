import json


# Este programa NO contiene la lista de productos.
#
# Los datos se encuentran guardados en compra.json.
# Vamos a recuperarlos desde allí.

with open("compra.json", "r", encoding="utf-8") as archivo:
    compra = json.load(archivo)


print("SUPERMERCADO:", compra["supermercado"])
print("FECHA:", compra["fecha"])

print()
print("PRODUCTOS")

for producto in compra["productos"]:
    print()
    print("Nombre:", producto["nombre"])
    print("Presentación:", producto["presentacion"])
    print("Precio: $", producto["precio"])
    print("Cantidad:", producto["cantidad"])
    print("¿Refrigerado?:", producto["refrigerado"])


# También podemos utilizar normalmente los datos cargados.

total = 0

for producto in compra["productos"]:
    total += producto["precio"] * producto["cantidad"]

print()
print("TOTAL DE LA COMPRA: $", total)


# ---------------------------------------------------------
# PARA PROBAR
# ---------------------------------------------------------
#
# EXPERIMENTO 1
#
# Abrí compra.json y modificá DIRECTAMENTE el nombre
# de algún producto.
#
# No ejecutes guardar_compra.py.
# Ejecutá solamente este archivo.
#
# ¿Aparece el cambio?
#
#
# ---------------------------------------------------------
# EXPERIMENTO 2
#
# Agregá manualmente un dato a uno de los productos:
#
#     "oferta": true
#
# Recordá agregar la coma correspondiente en el JSON.
#
# Ejecutá este programa.
#
# ¿Funciona?
# ¿El programa utiliza el dato "oferta"?
#
#
# ---------------------------------------------------------
# EXPERIMENTO 3
#
# Borrá el campo "precio" de UNO de los productos
# dentro de compra.json.
#
# Ejecutá nuevamente este programa.
#
# ¿Qué sucede?
# ¿En qué momento aparece el problema?
#
#
# ---------------------------------------------------------
# EXPERIMENTO 4
#
# Volvé a generar compra.json ejecutando guardar_compra.py.
#
# Después, modificá manualmente:
#
#     "cantidad": 2
#
# por:
#
#     "cantidad": "dos"
#
# El archivo sigue siendo un JSON válido.
#
# Ejecutá este programa.
#
# ¿Puede Python cargar el archivo?
# ¿Qué sucede cuando intenta calcular el total?