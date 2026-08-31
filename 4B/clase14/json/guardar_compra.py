import json


# Estos datos existen, por ahora, solamente dentro del programa.
compra = {
    "supermercado": "El Ahorro",
    "fecha": "19/08/2026",
    "productos": [
        {
            "nombre": "Leche",
            "presentacion": "1 litro",
            "precio": 1850.50,
            "cantidad": 2,
            "refrigerado": True
        },
        {
            "nombre": "Arroz",
            "presentacion": "1 kg",
            "precio": 2100,
            "cantidad": 1,
            "refrigerado": False
        },
        {
            "nombre": "Queso cremoso",
            "presentacion": "500 g",
            "precio": 5600,
            "cantidad": 1,
            "refrigerado": True
        },
        {
            "nombre": "Galletitas",
            "presentacion": "300 g",
            "precio": 1700,
            "cantidad": 3,
            "refrigerado": False
        }
    ]
}


# "w" significa que abrimos el archivo para escribir.
#
# Si compra.json no existe, Python lo crea.
# Si ya existe, su contenido anterior es reemplazado.
with open("compra.json", "w", encoding="utf-8") as archivo:
    json.dump(compra, archivo, indent=4, ensure_ascii=False)


print("Los datos fueron guardados en compra.json")


# ---------------------------------------------------------
# PARA PROBAR
# ---------------------------------------------------------
#
# 1. Ejecutá este programa.
#
# 2. Buscá el archivo compra.json y abrilo.
#    Comparalo con el diccionario "compra".
#
# 3. Después ejecutá leer_compra.py.
#
# 4. Volvé a este archivo y cambiá:
#
#       "nombre": "Leche"
#
#    por:
#
#       "nombre": "Leche descremada"
#
#    PERO NO EJECUTES ESTE PROGRAMA TODAVÍA.
#
# 5. Ejecutá solamente leer_compra.py.
#
#    ¿Qué nombre aparece?
#    ¿Por qué?
#
# 6. Ahora sí, ejecutá nuevamente este programa
#    y después ejecutá leer_compra.py.
#
#    ¿Qué cambió?