# Guía de actividades: funciones

## Objetivo

El objetivo de esta guía es practicar el diseño y la implementación de funciones en Python.

Se trabajará con funciones que reciben parámetros y devuelven resultados. Algunas funciones devolverán valores simples, como números, strings o booleanos. Otras devolverán estructuras como tuplas, listas o diccionarios.

## Indicaciones generales

- Cada consigna debe resolverse definiendo una función.
- Las funciones deben recibir los datos mediante parámetros.
- Las funciones deben devolver el resultado usando `return`.
- No se debe usar `input()` dentro de las funciones.
- No se debe usar `print()` dentro de las funciones, salvo que la consigna lo indique explícitamente.
- Los ejemplos dados sirven para probar el funcionamiento, pero no son los únicos casos posibles.
- En los ejercicios que usan listas o diccionarios, no se debe modificar la información original salvo que la consigna lo indique.

---

## 1. Análisis de un rectángulo

Se debe crear una función llamada `analizar_rectangulo`.

La función debe recibir dos parámetros:

- `base`
- `altura`

La función debe devolver una tupla con tres datos:

1. el área del rectángulo;
2. el perímetro del rectángulo;
3. un valor booleano que indique si el rectángulo es un cuadrado.

Ejemplo:

```python
resultado = analizar_rectangulo(5, 5)
print(resultado)
```

Salida esperada:

```python
(25, 20, True)
```

Otro ejemplo:

```python
resultado = analizar_rectangulo(4, 7)
print(resultado)
```

Salida esperada:

```python
(28, 22, False)
```

---

## 2. Datos de una caja rectangular

Se debe crear una función llamada `datos_caja`.

La función debe recibir tres parámetros:

- `largo`
- `ancho`
- `alto`

La función debe devolver una lista con tres datos:

1. el volumen de la caja;
2. la superficie total de la caja;
3. la suma total de las aristas.

Para una caja rectangular:

```python
volumen = largo * ancho * alto
superficie = 2 * (largo * ancho + largo * alto + ancho * alto)
aristas = 4 * (largo + ancho + alto)
```

Ejemplo:

```python
resultado = datos_caja(2, 3, 4)
print(resultado)
```

Salida esperada:

```python
[24, 52, 36]
```

Otro ejemplo:

```python
resultado = datos_caja(5, 2, 1)
print(resultado)
```

Salida esperada:

```python
[10, 34, 32]
```

---

## 3. Conversión de distancias

Se debe crear una función llamada `convertir_distancia`.

La función debe recibir tres parámetros:

- `valor`
- `origen`
- `destino`

Las unidades posibles son:

- `"cm"`
- `"m"`
- `"km"`

La función debe convertir el valor desde la unidad de origen hacia la unidad de destino.

Si alguna de las unidades no es válida, la función debe devolver:

```python
"unidad inválida"
```

Ejemplo:

```python
resultado = convertir_distancia(1000, "m", "km")
print(resultado)
```

Salida esperada:

```python
1.0
```

Otro ejemplo:

```python
resultado = convertir_distancia(2, "km", "m")
print(resultado)
```

Salida esperada:

```python
2000
```

Otro ejemplo:

```python
resultado = convertir_distancia(50, "cm", "mm")
print(resultado)
```

Salida esperada:

```python
unidad inválida
```

---

## 4. Resumen de una lista de números

Se debe crear una función llamada `resumen_lista`.

La función debe recibir una lista de números.

La función debe devolver un diccionario con la siguiente información:

- `"menor"`: el número más chico;
- `"mayor"`: el número más grande;
- `"cantidad"`: la cantidad de elementos;
- `"promedio"`: el promedio de los números.

Ejemplo:

```python
resultado = resumen_lista([4, 8, 10, 2])
print(resultado)
```

Salida esperada:

```python
{
    "menor": 2,
    "mayor": 10,
    "cantidad": 4,
    "promedio": 6.0
}
```

Otro ejemplo:

```python
resultado = resumen_lista([15, 5, 20, 10])
print(resultado)
```

Salida esperada:

```python
{
    "menor": 5,
    "mayor": 20,
    "cantidad": 4,
    "promedio": 12.5
}
```

---

## 5. Lecturas válidas de un sensor

Se debe crear una función llamada `filtrar_lecturas_validas`.

La función debe recibir una lista de lecturas de un sensor de distancia.

Una lectura se considera válida si está entre `2` y `400`, inclusive.

La función debe devolver una nueva lista que contenga solamente las lecturas válidas.

Ejemplo:

```python
resultado = filtrar_lecturas_validas([10, 0, 25, 500, 80])
print(resultado)
```

Salida esperada:

```python
[10, 25, 80]
```

Otro ejemplo:

```python
resultado = filtrar_lecturas_validas([1, 2, 3, 400, 401])
print(resultado)
```

Salida esperada:

```python
[2, 3, 400]
```

---

## 6. Análisis de distancias

Se debe crear una función llamada `analizar_distancias`.

La función debe recibir dos parámetros:

- `lecturas`
- `umbral`

El parámetro `lecturas` será una lista de números que representan mediciones de distancia.

La función debe ignorar las lecturas inválidas. Una lectura es válida si está entre `2` y `400`, inclusive.

La función debe devolver un diccionario con la siguiente información:

- `"validas"`: cantidad de lecturas válidas;
- `"obstaculos"`: cantidad de lecturas válidas menores que el umbral;
- `"promedio"`: promedio de las lecturas válidas.

Ejemplo:

```python
resultado = analizar_distancias([10, 0, 25, 500, 80], 30)
print(resultado)
```

Salida esperada:

```python
{
    "validas": 3,
    "obstaculos": 2,
    "promedio": 38.333333333333336
}
```

Otro ejemplo:

```python
resultado = analizar_distancias([5, 8, 12, 50, 700], 10)
print(resultado)
```

Salida esperada:

```python
{
    "validas": 4,
    "obstaculos": 2,
    "promedio": 18.75
}
```

---

## 7. Estado de un alumno

Se debe crear una función llamada `estado_alumno`.

La función debe recibir un diccionario que representa a un alumno.

El diccionario tendrá, como mínimo, las claves:

- `"nombre"`
- `"nota"`

La función debe devolver:

- `"aprobado"` si la nota es mayor o igual a `6`;
- `"desaprobado"` si la nota es menor que `6`.

Ejemplo:

```python
alumno = {
    "nombre": "Ana",
    "nota": 8
}

resultado = estado_alumno(alumno)
print(resultado)
```

Salida esperada:

```python
aprobado
```

Otro ejemplo:

```python
alumno = {
    "nombre": "Luis",
    "nota": 4
}

resultado = estado_alumno(alumno)
print(resultado)
```

Salida esperada:

```python
desaprobado
```

---

## 8. Nombres de alumnos aprobados

Se debe crear una función llamada `obtener_nombres_aprobados`.

La función debe recibir una lista de diccionarios. Cada diccionario representa a un alumno y tiene las claves:

- `"nombre"`
- `"nota"`

La función debe devolver una lista con los nombres de los alumnos aprobados.

Un alumno está aprobado si su nota es mayor o igual a `6`.

Ejemplo:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 5},
    {"nombre": "Marta", "nota": 9}
]

resultado = obtener_nombres_aprobados(alumnos)
print(resultado)
```

Salida esperada:

```python
["Ana", "Marta"]
```

Otro ejemplo:

```python
alumnos = [
    {"nombre": "Juan", "nota": 4},
    {"nombre": "Sofía", "nota": 6},
    {"nombre": "Pedro", "nota": 10}
]

resultado = obtener_nombres_aprobados(alumnos)
print(resultado)
```

Salida esperada:

```python
["Sofía", "Pedro"]
```

---

## 9. Resumen de un curso

Se debe crear una función llamada `resumen_curso`.

La función debe recibir una lista de diccionarios. Cada diccionario representa a un alumno y tiene las claves:

- `"nombre"`
- `"nota"`

La función debe devolver un diccionario con la siguiente información:

- `"total"`: cantidad total de alumnos;
- `"aprobados"`: cantidad de alumnos aprobados;
- `"desaprobados"`: cantidad de alumnos desaprobados;
- `"promedio"`: promedio general del curso.

Un alumno está aprobado si su nota es mayor o igual a `6`.

Ejemplo:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 5},
    {"nombre": "Marta", "nota": 9}
]

resultado = resumen_curso(alumnos)
print(resultado)
```

Salida esperada:

```python
{
    "total": 3,
    "aprobados": 2,
    "desaprobados": 1,
    "promedio": 7.333333333333333
}
```

Otro ejemplo:

```python
alumnos = [
    {"nombre": "Juan", "nota": 4},
    {"nombre": "Sofía", "nota": 6},
    {"nombre": "Pedro", "nota": 10},
    {"nombre": "Camila", "nota": 2}
]

resultado = resumen_curso(alumnos)
print(resultado)
```

Salida esperada:

```python
{
    "total": 4,
    "aprobados": 2,
    "desaprobados": 2,
    "promedio": 5.5
}
```

---

## 10. Notas válidas con campos faltantes

Se debe crear una función llamada `obtener_notas_validas`.

La función debe recibir una lista de diccionarios. Cada diccionario representa a un alumno.

Algunos diccionarios pueden no tener el campo `"nota"`.

La función debe devolver una lista con las notas que sí se encuentren disponibles.

Esta actividad debe resolverse usando `try` y `except`.

Ejemplo:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis"},
    {"nombre": "Marta", "nota": 9}
]

resultado = obtener_notas_validas(alumnos)
print(resultado)
```

Salida esperada:

```python
[8, 9]
```

Otro ejemplo:

```python
alumnos = [
    {"nombre": "Juan"},
    {"nombre": "Sofía", "nota": 6},
    {"nombre": "Pedro", "nota": 10},
    {"nombre": "Camila"}
]

resultado = obtener_notas_validas(alumnos)
print(resultado)
```

Salida esperada:

```python
[6, 10]
```

Otro ejemplo:

```python
alumnos = [
    {"nombre": "Ana"},
    {"nombre": "Luis"},
    {"nombre": "Marta"}
]

resultado = obtener_notas_validas(alumnos)
print(resultado)
```

Salida esperada:

```python
[]
```

---

## 11. Búsqueda de un alumno

Se debe crear una función llamada `buscar_alumno`.

La función debe recibir dos parámetros:

- `alumnos`: una lista de diccionarios;
- `nombre`: el nombre que se desea buscar.

Cada diccionario de la lista representa a un alumno.

La función debe devolver el diccionario completo del alumno si lo encuentra.

Si no encuentra ningún alumno con ese nombre, debe devolver `None`.

Ejemplo:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 5}
]

resultado = buscar_alumno(alumnos, "Luis")
print(resultado)
```

Salida esperada:

```python
{"nombre": "Luis", "nota": 5}
```

Otro ejemplo:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 5}
]

resultado = buscar_alumno(alumnos, "Marta")
print(resultado)
```

Salida esperada:

```python
None
```

---

## 12. Agregar estado a los alumnos

Se debe crear una función llamada `agregar_estado`.

La función debe recibir una lista de diccionarios. Cada diccionario representa a un alumno y tiene las claves:

- `"nombre"`
- `"nota"`

La función debe devolver una nueva lista de diccionarios.

Cada diccionario de la nueva lista debe tener los mismos datos del alumno original, pero además debe incluir una nueva clave llamada `"estado"`.

El estado debe ser:

- `"aprobado"` si la nota es mayor o igual a `6`;
- `"desaprobado"` si la nota es menor que `6`.

La función no debe modificar la lista original.

Ejemplo:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 5}
]

resultado = agregar_estado(alumnos)
print(resultado)
```

Salida esperada:

```python
[
    {"nombre": "Ana", "nota": 8, "estado": "aprobado"},
    {"nombre": "Luis", "nota": 5, "estado": "desaprobado"}
]
```

Para verificar que la lista original no se haya modificado, se puede probar:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 5}
]

resultado = agregar_estado(alumnos)

print(resultado)
print(alumnos)
```

La segunda impresión no debería contener la clave `"estado"`.

---

## 13. Valor total de un stock

Se debe crear una función llamada `valor_total_stock`.

La función debe recibir una lista de diccionarios. Cada diccionario representa a un producto y tiene las claves:

- `"nombre"`
- `"precio"`
- `"stock"`

La función debe devolver el valor total del inventario.

El valor total de cada producto se calcula como:

```python
precio * stock
```

Ejemplo:

```python
productos = [
    {"nombre": "led", "precio": 80, "stock": 10},
    {"nombre": "motor", "precio": 2500, "stock": 2}
]

resultado = valor_total_stock(productos)
print(resultado)
```

Salida esperada:

```python
5800
```

Otro ejemplo:

```python
productos = [
    {"nombre": "resistor", "precio": 20, "stock": 100},
    {"nombre": "sensor", "precio": 1500, "stock": 3},
    {"nombre": "cable", "precio": 300, "stock": 5}
]

resultado = valor_total_stock(productos)
print(resultado)
```

Salida esperada:

```python
8000
```

---

## 14. Productos con bajo stock

Se debe crear una función llamada `productos_bajo_stock`.

La función debe recibir dos parámetros:

- `productos`: una lista de diccionarios;
- `minimo`: un número que representa el stock mínimo deseado.

Cada diccionario representa a un producto y tiene las claves:

- `"nombre"`
- `"precio"`
- `"stock"`

La función debe devolver una lista con los productos cuyo stock sea menor que `minimo`.

Ejemplo:

```python
productos = [
    {"nombre": "led", "precio": 80, "stock": 10},
    {"nombre": "motor", "precio": 2500, "stock": 2},
    {"nombre": "resistor", "precio": 20, "stock": 100}
]

resultado = productos_bajo_stock(productos, 20)
print(resultado)
```

Salida esperada:

```python
[
    {"nombre": "led", "precio": 80, "stock": 10},
    {"nombre": "motor", "precio": 2500, "stock": 2}
]
```

Otro ejemplo:

```python
productos = [
    {"nombre": "sensor", "precio": 1500, "stock": 4},
    {"nombre": "cable", "precio": 300, "stock": 30},
    {"nombre": "buzzer", "precio": 600, "stock": 8}
]

resultado = productos_bajo_stock(productos, 10)
print(resultado)
```

Salida esperada:

```python
[
    {"nombre": "sensor", "precio": 1500, "stock": 4},
    {"nombre": "buzzer", "precio": 600, "stock": 8}
]
```

---

## 15. Resumen de inventario

Se debe crear una función llamada `resumen_inventario`.

La función debe recibir una lista de diccionarios. Cada diccionario representa a un producto y tiene las claves:

- `"nombre"`
- `"precio"`
- `"stock"`

La función debe devolver un diccionario con la siguiente información:

- `"cantidad_productos"`: cantidad de productos distintos;
- `"valor_total"`: valor total del inventario;
- `"producto_mas_caro"`: nombre del producto con mayor precio;
- `"productos_sin_stock"`: lista con los nombres de los productos cuyo stock sea `0`.

Ejemplo:

```python
productos = [
    {"nombre": "led", "precio": 80, "stock": 10},
    {"nombre": "motor", "precio": 2500, "stock": 2},
    {"nombre": "resistor", "precio": 20, "stock": 0}
]

resultado = resumen_inventario(productos)
print(resultado)
```

Salida esperada:

```python
{
    "cantidad_productos": 3,
    "valor_total": 5800,
    "producto_mas_caro": "motor",
    "productos_sin_stock": ["resistor"]
}
```

Otro ejemplo:

```python
productos = [
    {"nombre": "sensor", "precio": 1500, "stock": 4},
    {"nombre": "cable", "precio": 300, "stock": 0},
    {"nombre": "buzzer", "precio": 600, "stock": 0},
    {"nombre": "display", "precio": 2200, "stock": 1}
]

resultado = resumen_inventario(productos)
print(resultado)
```

Salida esperada:

```python
{
    "cantidad_productos": 4,
    "valor_total": 8200,
    "producto_mas_caro": "display",
    "productos_sin_stock": ["cable", "buzzer"]
}
```

---

## Criterios de revisión

Para revisar cada actividad, se debe verificar que:

- la función tenga el nombre pedido;
- la función reciba los parámetros indicados;
- la función devuelva el tipo de dato solicitado;
- la función no use `input()` internamente;
- la función no use `print()` internamente, salvo que se indique;
- los ejemplos de prueba produzcan la salida esperada;
- en los ejercicios con listas o diccionarios, no se modifiquen los datos originales salvo que la consigna lo pida.