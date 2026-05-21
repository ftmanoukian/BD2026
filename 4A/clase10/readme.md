# Consigna de desarrollo 2

## Objetivos
Se debe escribir un programa que analice el desempeño académico de un curso, a partir de los datos cargados en un archivo `.csv`. Para esto se debe:
- Utilizar los conocimientos ya adquiridos respecto a todas las herramientas vistas en clase.
- Investigar la utilización de herramientas adicionales, utilizando preguntas guía como apoyo para la investigación. Se sugiere anotar y guardar las respuestas a estas preguntas guía. 

En caso de utilizar IA o internet para investigar, anotar qué preguntaron y qué respuesta les sirvió.

## Consigna

### 1. Creación del archivo de datos
Crear un archivo llamado `notas_curso.csv`. El mismo debe tener las siguientes columnas:
  - Nombre del alumno
  - Nota de matemática
  - Nota de lengua
  - Nota de BD
  - Nota de TI

Se debe, a su vez, rellenar el contenido correspondiente a al menos 6 alumnos.
    
⚠️ La tabla debe ser creada manualmente por cada alumno ⚠️

La primera fila del archivo debe ser:

    nombre,matematica,lengua,bd,ti

#### Preguntas guía:
- ¿Qué es un `csv`? ¿Para qué sirve? ¿Cuál es la diferencia con un `xls` (excel)?
- ¿Cómo se abre y edita? (Sugerencia: utilizar VS Code)
- ¿Cómo se delimita la información dentro del archivo? ¿Importa el espaciado horizontal? ¿Qué caracteres se pueden utilizar para delimitar elementos?
---

### 2. Importación del archivo de datos
Escribir un programa `importacion_datos.py` que utilice el módulo `csv` de python para leer el archivo e importar los datos al mismo.

Los datos deben leerse de la siguiente forma:
- Un diccionario por cada fila (pista: `csv.DictReader`)
- Una lista que represente a la tabla, y contenga a los diccionarios de cada fila

Para verificar que se leyeron correctamente los datos, el programa debe imprimir los mismos en el terminal.

#### Preguntas guía:

- ¿Qué es un módulo de Python?
- ¿Qué formas existen de importar un módulo a un programa?
- ¿En qué carpeta debe ubicarse el archivo `.csv` que creamos anteriormente, para que el programa de python pueda leerlo?

---

### 3. Análisis de notas

Escribir un programa `analisis_notas.py` que:
- Importe los datos del `csv` en una lista de diccionarios
- Calcule el promedio de cada alumno, indicando si está aprobado (promedio >= 6) o no
- Calcule el promedio general del curso (es decir, el promedio de todos los promedios)

El archivo `csv` debe incluir datos que permitan verificar el funcionamiento del programa:
- al menos un alumno aprobado
- al menos un alumno desaprobado
- al menos un alumno con notas distintas entre materias

#### Preguntas guía:
- Los datos importados, ¿se pueden usar tal como fueron importados? ¿es necesario realizar alguna acción con los mismos?

---

### 4. Detección de errores - Desafío

Modificar el proceso de importación del `csv` para **validar** los datos antes de importarlos a la lista. 

En caso de que alguna nota no sea pueda convertir al tipo adecuado, se debe saltear la importación de dicho alumno, informando por el terminal:
- Nombre del alumno
- Qué dato no tiene el tipo adecuado

Para esto, investigar el funcionamiento de `try/except`. Para verificar que el programa funciona correctamente, se debe forzar un error dentro del `csv`.

#### Preguntas guía
- ¿Para qué sirve `try/except`?
- ¿Por qué no se pueden utilizar los datos tal cual son importados?
- ¿Qué diferencia hay entre que el programa se detenga y que el programa informe el error y continúe?
