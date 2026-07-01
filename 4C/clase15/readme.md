# Simulacro de examen - Python

## Ejercicio 1

Completá el código utilizando alguno de los métodos disponibles para obtener el resultado esperado.

```python
texto = "Hola mundo"
resultado = texto.__________
# Resultado esperado en resultado: "Hola Python"
```

### Métodos disponibles

- `upper()`: devuelve el string en mayúsculas.
- `lower()`: devuelve el string en minúsculas.
- `strip()`: elimina espacios al principio y al final.
- `replace(viejo, nuevo)`: reemplaza una parte por otra.

---

## Ejercicio 2

Analizá el siguiente bloque de código y respondé las preguntas a continuación.

### Aclaración

- `isinstance(x, tipo)` devuelve `True` si `x` es del tipo indicado.
- `isalpha()` devuelve `True` si todos los caracteres del string son letras del alfabeto.
- `upper()` devuelve una copia del string con todas las letras convertidas a mayúsculas.

```python
def filtrar_texto(lista):
    nueva = []

    for x in lista:
        if isinstance(x, str) and x.isalpha():
            nueva.append(x.upper())
        elif isinstance(x, int) and x > 10:
            nueva.append(str(x))

    return nueva

print(filtrar_texto(["hola", 8, "23", 15, "mundo", 3.5, True]))
```

### Preguntas

a) ¿Qué valores aparecen en pantalla al ejecutar este programa?

b) ¿Por qué el valor `3.5` no se incluye en la lista resultante?

c) ¿Qué ocurriría si se elimina la condición `x.isalpha()` y se intenta convertir `"23"`?

---

## Ejercicio 3

Escribí el resultado de las siguientes expresiones.

Si alguna da error, indicá `"ERROR"`.

a)

```python
"tecnología"[2:6]
```

b)

```python
str(5.8)[1]
```

c)

```python
[5, 15, 25][::-2]
```

d)

```python
"123abc".isalpha()
```

e)

```python
len("robotica"[4:])
```

f)

```python
[8, 16, 24][1] + int("63")
```

g)

```python
"4 * 2" + str(4 * 2)
```

h)

```python
"bot"[0] * 4
```

i)

```python
"microcontrolador"[2::3]
```

j)

```python
int("6") + float("4.5")
```

k)

```python
["x", "y", "z"][1] + "a"
```

---

## Ejercicio 4

Interpretá la funcionalidad del siguiente bloque de código:

```python
def consigna4(texto):

    cnt = 0

    for l in texto:

        if l == "a":
            cnt += 1

        else:
            cnt = cnt

    return cnt
```

¿Qué resultado obtendremos si llamamos a la función con los siguientes parámetros?

a)

```python
consigna4("hola como estás?")
```

b)

```python
consigna4("érase una vez en meca")
```

c)

```python
consigna4("123456789")
```

---

## Ejercicio 5

Analizá el siguiente bloque de código y respondé la pregunta.

```python
def sumar_enteros(lista):
    suma = 0

    for dato in lista:
        try:
            numero = int(dato)
            suma += numero

        except:
            continue

    return suma

resultado = sumar_enteros(["12", "hola", "7", "3.5", "0", "robot"])
print(resultado)
```

¿Qué muestra en pantalla este programa?

a) `19`

b) `22`

c) `12`

d) Da error porque `"hola"` no se puede convertir a entero.

---

## Ejercicio 6

Completá el código utilizando alguno de los métodos disponibles para obtener el resultado esperado.

```python
numeros = [4, 8, 15, 16]
numeros.__________
# Resultado esperado en numeros: [4, 8, 15, 16, 23]
```

### Métodos disponibles

- `append(elemento)`: agrega un elemento al final de la lista.
- `remove(elemento)`: elimina la primera aparición de un elemento.
- `pop(posicion)`: elimina y devuelve el elemento de una posición.
- `insert(posicion, elemento)`: inserta un elemento en una posición determinada.

---

## Ejercicio 7

Completá el código utilizando alguno de los métodos disponibles para obtener el resultado esperado.

```python
alumno = {
    "nombre": "Lucía",
    "curso": "4°A"
}

alumno.__________

# Resultado esperado en alumno:
# {"nombre": "Lucía", "curso": "4°A", "nota": 8}
```

### Métodos disponibles

- `keys()`: devuelve las claves del diccionario.
- `values()`: devuelve los valores del diccionario.
- `items()`: devuelve pares clave-valor del diccionario.
- `update(diccionario)`: agrega o modifica pares clave-valor.

---

## Ejercicio 8

Analizá el siguiente bloque de código:

```python
def revisar_temperaturas(lista):
    altas = []

    for temperatura in lista:
        if temperatura >= 30:
            altas.append(temperatura)

    return altas

print(revisar_temperaturas([24, 31, 28, 35, 30, 22]))
```

¿Qué muestra en pantalla este programa?

a) `[31, 35, 30]`

b) `[24, 28, 22]`

c) `[30, 31, 35]`

d) `3`

---

## Ejercicio 9

Crear una función llamada `clasificar_caja`.

La función debe recibir tres parámetros:

- `largo`
- `ancho`
- `alto`

La función debe calcular el volumen de la caja y devolver un diccionario con la siguiente información:

- `"volumen"`: el volumen de la caja.
- `"tipo"`: `"chica"` si el volumen es menor que `100`.
- `"tipo"`: `"grande"` si el volumen es mayor o igual que `100`.

Ejemplo:

```python
resultado = clasificar_caja(2, 3, 4)
print(resultado)
```

Salida esperada:

```python
{
    "volumen": 24,
    "tipo": "chica"
}
```

Otro ejemplo:

```python
resultado = clasificar_caja(5, 5, 5)
print(resultado)
```

Salida esperada:

```python
{
    "volumen": 125,
    "tipo": "grande"
}
```

---

## Ejercicio 10

Crear una función llamada `volumen_total_macetas`.

La función debe recibir una lista de tuplas. Cada tupla representa una maceta.

Si la tupla tiene 2 elementos, representa una maceta cilíndrica:

```python
(radio, altura)
```

En ese caso, el volumen se calcula así:

```python
3.14 * radio * radio * altura
```

Si la tupla tiene 3 elementos, representa una maceta rectangular:

```python
(base, ancho, alto)
```

En ese caso, el volumen se calcula así:

```python
base * ancho * alto
```

La función debe devolver el volumen total de todas las macetas.

Todas las tuplas tendrán 2 o 3 elementos. No hace falta contemplar otros casos.

Ejemplo:

```python
macetas = [
    (2, 10),
    (3, 4, 5),
    (1, 8)
]

resultado = volumen_total_macetas(macetas)
print(resultado)
```

Salida esperada:

```python
210.72
```

Otro ejemplo:

```python
macetas = [
    (4, 5),
    (2, 3, 10)
]

resultado = volumen_total_macetas(macetas)
print(resultado)
```

Salida esperada:

```python
311.2
```