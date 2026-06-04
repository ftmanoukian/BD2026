[Pizarrón con la resolución de la actividad integradora](https://www.tldraw.com/p/U_mlr7FIwc0kl31NflrOT?d=v-3323.-394.8121.3836.QujU54mn53hwoWvnH9IZc)

# Actividad: datos abiertos con Python, pandas y Google Colab

## Objetivo

En esta actividad vamos a usar una biblioteca de Python llamada **pandas** para trabajar con un archivo de datos real.

La idea es responder una pregunta sencilla usando:

- una tabla de datos;
- un conteo o cálculo simple;
- un gráfico fácil de interpretar;
- una conclusión escrita en palabras.

No hace falta hacer análisis estadístico avanzado.

---

## Herramienta recomendada: Google Colab desde el navegador

La forma más sencilla de trabajar es usar Google Colab directamente desde el navegador:

<https://colab.research.google.com/>

Para usarlo:

1. Entrar a Google Colab.
2. Iniciar sesión con una cuenta de Google.
3. Abrir el notebook plantilla.
4. Subir el archivo CSV.
5. Ejecutar las celdas en orden.

---

## Opción alternativa: Google Colab en VS Code

También existe una extensión de Google Colab para VS Code.

Esta opción es opcional. Para esta actividad recomendamos usar Colab desde el navegador porque es más simple y evita problemas de configuración.

---

## Portal de datasets de CABA

Los datasets se pueden buscar en el portal de datos abiertos de la Ciudad de Buenos Aires:

<https://data.buenosaires.gob.ar/>

Cada grupo debe elegir un dataset que pueda entender y usar para responder una pregunta sencilla.

---

## Cómo cargar un archivo CSV en Google Colab

1. Descargar el archivo CSV del portal de datos.
2. Abrir el notebook en Google Colab.
3. En el panel izquierdo, hacer clic en el ícono de carpeta.
4. Presionar el botón para subir archivos.
5. Seleccionar el archivo CSV.
6. En el notebook, escribir el nombre del archivo:

```python
df = pd.read_csv("nombre_del_archivo.csv")
```

Importante: el nombre debe coincidir exactamente con el archivo subido.

---

## Notebook plantilla

Usen el notebook plantilla para completar la actividad:

**Enlace al notebook plantilla:**  
[Enlace](./plantilla.ipynb)

---

## Datasets sugeridos

Para evitar datasets demasiado difíciles, se sugieren estos temas:

- arbolado público;
- estaciones de Ecobici;
- espacios verdes;
- establecimientos educativos;
- bibliotecas;
- actividades culturales;
- reclamos o solicitudes vecinales, si el archivo es fácil de entender.

También pueden elegir otro dataset del portal, pero antes verifiquen que sea entendible.

---

## Cómo elegir un buen dataset

Antes de empezar, revisen:

- ¿Se puede abrir el archivo con pandas?
- ¿Se entiende qué representa cada fila?
- ¿Tiene columnas con categorías, como comuna, barrio, tipo o nombre?
- ¿Permite contar valores o comparar categorías?
- ¿No requiere limpieza complicada?

Para esta actividad conviene evitar datasets con muchas tablas, códigos difíciles de entender o archivos demasiado complejos.

---

## Qué pregunta o hipótesis elegir

La pregunta debe ser sencilla y verificable con pandas.

Ejemplos recomendados:

- ¿Cuál es la comuna con más registros?
- ¿Cuáles son los 10 valores más frecuentes?
- ¿Qué categoría aparece más veces?
- ¿Hay mucha diferencia entre categorías?
- ¿Cuál es el barrio con más registros?
- ¿Cuál es el tipo más común?

Ejemplos de hipótesis simples:

- Creemos que una comuna concentra más registros que las demás.
- Creemos que algunas categorías son mucho más frecuentes que otras.
- Creemos que hay más registros en una categoría que en otra.

---

## Qué evitar

Eviten hipótesis demasiado difíciles, por ejemplo:

- “Esto causa aquello”.
- “Este barrio es mejor que otro”.
- “Este servicio funciona peor por culpa de...”
- “Las comunas con más X tienen mejor calidad de vida”.
- “Las bicisendas reducen accidentes”.

Esas preguntas pueden ser interesantes, pero requieren más datos y métodos más avanzados.

---

## Código mínimo esperado

Durante la actividad deberían usar algo parecido a esto:

```python
import pandas as pd
```

```python
df = pd.read_csv("archivo.csv")
```

```python
df.head()
```

```python
df.columns
```

```python
df["columna"].value_counts()
```

```python
df["columna"].value_counts().head(10).plot(kind="bar")
```

---

## Presentación grupal

Cada grupo tendrá 5 minutos para presentar.

La presentación debe incluir:

1. Nombre del dataset elegido.
2. Qué representa cada fila.
3. Qué columna o columnas usaron.
4. Pregunta o hipótesis planteada.
5. Tabla o gráfico obtenido.
6. Conclusión final.

No se evalúa que la hipótesis “se cumpla”.  
Se evalúa que puedan hacer una pregunta clara, usar pandas y explicar el resultado.

---

## Nivel extra opcional

Quienes quieran avanzar más pueden usar:

```python
df.groupby("columna")["otra_columna"].mean()
```

Esto permite calcular promedios por categoría.

Por ejemplo:

- promedio de altura por especie;
- promedio de superficie por comuna;
- promedio de cantidad por tipo.

Este nivel es opcional.
