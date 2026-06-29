# Clase 12

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
lista = ["hola", 8, "23", 15, "mundo", 3.5, True]
nueva = []

for x in lista:
    if isinstance(x, str) and x.isalpha():
        nueva.append(x.upper())
    elif isinstance(x, int) and x > 10:
        nueva.append(str(x))

print(nueva)
```

### Preguntas

a) ¿Qué valores aparecen en pantalla al ejecutar este programa?

b) ¿Por qué el valor `3.5` no se incluye en la lista resultante?

c) ¿Por qué el string `"23"` no se incluye en la lista resultante?

d) ¿Qué diferencia hay entre agregar `x` y agregar `str(x)` en la lista?

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
texto = "hola como estás?"

cnt = 0

for l in texto:
    if l == "a":
        cnt += 1
    else:
        cnt = cnt

print(cnt)
```

### Preguntas

a) ¿Qué muestra en pantalla este programa?

b) ¿Qué está contando la variable `cnt`?

c) ¿Para qué sirve la línea `cnt += 1`?

d) ¿Qué pasaría si el texto fuera `"123456789"`?

e) ¿Qué pasaría si el texto fuera `"érase una vez en meca"`?

---

## Ejercicio 5

Analizá el siguiente bloque de código y respondé la pregunta.

```python
datos = ["12", "hola", "7", "3.5", "0", "robot"]

suma = 0

for dato in datos:
    try:
        numero = int(dato)
        suma += numero

    except:
        continue

print(suma)
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
temperaturas = [24, 31, 28, 35, 30, 22]
altas = []

for temperatura in temperaturas:
    if temperatura >= 30:
        altas.append(temperatura)

print(altas)
```

¿Qué muestra en pantalla este programa?

a) `[31, 35, 30]`

b) `[24, 28, 22]`

c) `[30, 31, 35]`

d) `3`

---

## Ejercicio 9

Analizá el siguiente bloque de código:

```python
palabras = ["motor", "eje", "sensor", "led", "rueda"]
largas = []

for palabra in palabras:
    if len(palabra) > 4:
        largas.append(palabra)

print(largas)
```

¿Qué muestra en pantalla este programa?

a) `["motor", "sensor", "rueda"]`

b) `["sensor", "rueda"]`

c) `["eje", "led"]`

d) `3`

---

## Ejercicio 10

Completá el código utilizando alguno de los métodos disponibles para obtener el resultado esperado.

```python
texto = "   sensor ultrasonico   "
resultado = texto.__________

# Resultado esperado en resultado: "sensor ultrasonico"
```

### Métodos disponibles

- `upper()`: devuelve el string en mayúsculas.
- `lower()`: devuelve el string en minúsculas.
- `strip()`: elimina espacios al principio y al final.
- `replace(viejo, nuevo)`: reemplaza una parte por otra.

---

## Ejercicio 11

Analizá el siguiente bloque de código:

```python
valores = ["10", "20", "hola", "5"]
total = 0

for valor in valores:
    if valor.isnumeric():
        total += int(valor)

print(total)
```

¿Qué muestra en pantalla este programa?

a) `35`

b) `30`

c) `"10205"`

d) Da error porque `"hola"` no se puede convertir a entero.

---

## Ejercicio 12

Completá el código utilizando alguno de los métodos disponibles para obtener el resultado esperado.

```python
componentes = ["motor", "sensor", "rueda"]
componentes.__________

# Resultado esperado en componentes: ["motor", "rueda"]
```

### Métodos disponibles

- `append(elemento)`: agrega un elemento al final de la lista.
- `remove(elemento)`: elimina la primera aparición de un elemento.
- `pop(posicion)`: elimina y devuelve el elemento de una posición.
- `insert(posicion, elemento)`: inserta un elemento en una posición determinada.

---

## Ejercicio 13

Analizá el siguiente bloque de código:

```python
alumno = {
    "nombre": "Tomás",
    "curso": "4°A",
    "nota": 6
}

if alumno["nota"] >= 6:
    alumno["estado"] = "aprobado"
else:
    alumno["estado"] = "desaprobado"

print(alumno)
```

¿Qué muestra en pantalla este programa?

a) `{"nombre": "Tomás", "curso": "4°A", "nota": 6, "estado": "aprobado"}`

b) `{"nombre": "Tomás", "curso": "4°A", "estado": "aprobado"}`

c) `{"estado": "aprobado"}`

d) Da error porque no se puede agregar una clave nueva a un diccionario.

---

## Ejercicio 14

Analizá el siguiente bloque de código:

```python
datos = ["8", "dos", "10", "3.5", "4"]

numeros = []

for dato in datos:
    try:
        numero = int(dato)
        numeros.append(numero)
    except:
        pass

print(numeros)
```

¿Qué muestra en pantalla este programa?

a) `[8, 10, 4]`

b) `[8, 10, 3.5, 4]`

c) `["8", "10", "4"]`

d) Da error porque `"dos"` no se puede convertir a entero.

---

## Ejercicio 15

Interpretá qué hace el siguiente bloque de código:

```python
mediciones = [12, 18, 25, 9, 30, 15]
contador = 0

for medicion in mediciones:
    if medicion >= 20:
        contador += 1

print(contador)
```

### Preguntas

a) ¿Qué muestra en pantalla este programa?

b) ¿Qué representa la variable `contador`?

c) ¿Qué valores de la lista cumplen la condición?

---

## Ejercicio 16

Completá el código utilizando alguno de los métodos disponibles para obtener el resultado esperado.

```python
texto = "sensor de temperatura"
resultado = texto.__________

# Resultado esperado en resultado: "SENSOR DE TEMPERATURA"
```

### Métodos disponibles

- `upper()`: devuelve el string en mayúsculas.
- `lower()`: devuelve el string en minúsculas.
- `strip()`: elimina espacios al principio y al final.
- `replace(viejo, nuevo)`: reemplaza una parte por otra.

---