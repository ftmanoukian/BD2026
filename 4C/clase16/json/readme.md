# Guardar datos con JSON

Hasta ahora, la mayoría de los datos que utilizamos existían mientras nuestro programa estaba ejecutándose.

¿Qué sucede cuando el programa termina?

En esta actividad vamos a utilizar archivos JSON para guardar información y recuperarla más adelante.


## JSON

JSON es un formato para representar datos.

Se parece mucho a las estructuras que ya conocemos de Python.

Por ejemplo, en Python podemos tener:

~~~python
producto = {
    "nombre": "Leche",
    "precio": 1850.50,
    "cantidad": 2,
    "refrigerado": True
}
~~~

En un archivo JSON podemos encontrar algo muy parecido:

~~~json
{
    "nombre": "Leche",
    "precio": 1850.50,
    "cantidad": 2,
    "refrigerado": true
}
~~~

Prestá atención a una diferencia:

- Python utiliza `True` y `False`.
- JSON utiliza `true` y `false`.

Los datos también pueden contener otros conjuntos de datos:

~~~json
{
    "supermercado": "El Ahorro",
    "productos": [
        {
            "nombre": "Leche",
            "cantidad": 2
        },
        {
            "nombre": "Arroz",
            "cantidad": 1
        }
    ]
}
~~~

En este ejemplo:

- `"supermercado"` contiene un texto.
- `"productos"` contiene una lista.
- Cada elemento de esa lista contiene los datos de un producto.


## Primera parte

Abrí y ejecutá:

`guardar_compra.py`

Después buscá el archivo:

`compra.json`

Abrilo y observá su contenido.

¿De dónde salieron esos datos?


## Segunda parte

Ejecutá:

`leer_compra.py`

Este programa no tiene escrita la lista de productos.

Entonces:

**¿de dónde obtiene la información que muestra?**


## Guardar y cargar

Para trabajar con JSON primero importamos el módulo:

~~~python
import json
~~~

Para guardar datos:

~~~python
json.dump(datos, archivo)
~~~

Para cargar datos:

~~~python
datos = json.load(archivo)
~~~

No es necesario memorizar estas instrucciones.

Lo importante es entender qué ocurre:

~~~text
DATOS EN PYTHON
      |
      | guardar
      v
ARCHIVO JSON
      |
      | cargar
      v
DATOS EN PYTHON
~~~


## Una pregunta importante

Supongamos que modificamos una variable dentro de `guardar_compra.py`.

¿Eso modifica automáticamente `compra.json`?

Probalo antes de responder.


## Los datos que esperamos recibir

Nuestro programa supone que cada producto tiene ciertos datos:

~~~text
nombre          texto
presentacion    texto
precio          número
cantidad        número entero
refrigerado     verdadero/falso
~~~

Pero JSON no conoce estas reglas.

Un archivo podría contener:

~~~json
{
    "nombre": "Leche",
    "cantidad": "dos"
}
~~~

Eso puede ser un JSON perfectamente válido.

Sin embargo, puede no servir para nuestro programa.

Por eso hay una diferencia entre:

**un archivo JSON válido**

y

**datos válidos para nuestro programa**.

También pueden ocurrir otras dos situaciones:

- aparece información que nuestro programa no utiliza;
- falta información que nuestro programa esperaba encontrar.

Probá ambas situaciones siguiendo las indicaciones de `leer_compra.py`.