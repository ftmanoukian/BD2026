# Actividad: análisis de datos abiertos con Python y pandas

## Objetivo

El objetivo de esta actividad es aprender a usar un notebook de Python para analizar datos reales.

La tarea consiste en elegir un dataset abierto de la Ciudad de Buenos Aires, formular hipótesis simples y verificarlas con operaciones básicas de pandas.

No se evalúa que la hipótesis “se cumpla”. Se evalúa que la pregunta esté bien planteada, que el método sea razonable y que la conclusión sea honesta.

---

## Herramientas necesarias

Para esta actividad vamos a usar:

- Google Colab;
- Python;
- pandas;
- matplotlib;
- un archivo CSV descargado desde Buenos Aires Data.

La opción recomendada es usar **Google Colab desde el navegador**, porque no requiere instalación local.

---

## Portal de datasets de CABA

Los datasets se pueden buscar en el portal oficial de Buenos Aires Data:

<https://data.buenosaires.gob.ar/dataset/>

Para esta actividad conviene elegir datasets en formato **CSV** o **XLSX**. Si pueden elegir, usen CSV.

---

## Dataset alternativo recomendado

Para evitar repetir el mismo análisis mostrado por el docente, se recomienda trabajar con un dataset distinto al de arbolado.

Algunas opciones sugeridas:

- **Estaciones de Bicicletas Públicas**: ubicación, nombre, ID, dirección, latitud y longitud de estaciones de Ecobici.  
  <https://data.buenosaires.gob.ar/dataset/estaciones-bicicletas-publicas>

- **Bicicletas Públicas**: usuarios y recorridos del sistema Ecobici en distintos años.  
  <https://data.buenosaires.gob.ar/dataset/bicicletas-publicas>

- **Puntos Verdes**: ubicación de puntos de recepción de materiales reciclables.  
  <https://data.buenosaires.gob.ar/dataset/puntos-verdes>

- **Espacios Verdes**: límites y ubicación geográfica de plazas, parques, jardines, canteros y otros espacios verdes.  
  <https://data.buenosaires.gob.ar/dataset/espacios-verdes>

- **Establecimientos Educativos**: ubicación geográfica de establecimientos educativos de la Ciudad.  
  <https://data.buenosaires.gob.ar/dataset/establecimientos-educativos>

También pueden elegir otro dataset del portal, pero antes de avanzar revisen que cumpla los criterios de la sección siguiente.

---

## Criterios para elegir dataset

Antes de empezar, verifiquen que el dataset cumpla con estas condiciones:

- Se puede descargar en CSV o XLSX.
- Se entiende qué representa cada fila.
- Tiene columnas útiles para comparar.
- Tiene al menos una columna categórica, por ejemplo comuna, barrio, tipo, categoría, especie, estado o nivel.
- Tiene al menos una columna numérica o temporal, por ejemplo cantidad, edad, superficie, año, mes, fecha, latitud o longitud.
- No requiere una limpieza demasiado compleja para poder empezar.

Preguntas iniciales obligatorias:

1. ¿Qué representa cada fila?
2. ¿Qué columnas parecen importantes?
3. ¿Qué columnas permiten agrupar?
4. ¿Qué columnas permiten medir o comparar?
5. ¿Hay valores faltantes en columnas importantes?

---

## Abrir Google Colab desde el navegador

1. Entrar a: <https://colab.research.google.com/>
2. Iniciar sesión con una cuenta de Google.
3. Elegir **Archivo → Subir notebook**.
4. Subir la plantilla de la actividad.
5. Guardar una copia propia si Colab lo solicita.

---

## Usar Google Colab desde VS Code (opcional)

También existe una extensión oficial de Google Colab para VS Code:

<https://marketplace.visualstudio.com/items?itemName=Google.colab>

Para usarla:

1. Abrir VS Code.
2. Ir a la pestaña de extensiones.
3. Buscar **Google Colab**.
4. Instalar la extensión oficial.
5. Instalar también la extensión de Jupyter si VS Code lo solicita.
6. Abrir el notebook `.ipynb`.
7. Conectarlo a un runtime de Colab desde las opciones del notebook.

Para esta actividad, el camino recomendado sigue siendo **Colab desde el navegador**, porque es más simple y evita problemas de configuración.

---

## Cómo cargar un archivo CSV en Google Colab

Primero, descarguen el archivo CSV desde Buenos Aires Data.

Luego, en el notebook, ejecuten esta celda:

```python
from google.colab import files

uploaded = files.upload()
filename = list(uploaded.keys())[0]
filename
```

Después, carguen el archivo con pandas:

```python
import pandas as pd

df = pd.read_csv(filename)
df.head()
```

Si aparece un error de codificación o separador, pueden probar:

```python
df = pd.read_csv(filename, encoding="latin1")
df.head()
```

O también:

```python
df = pd.read_csv(filename, sep=";")
df.head()
```

---

## Notebook plantilla

Descargar y usar esta plantilla:

[plantilla_actividad_pandas_caba.ipynb](./plantilla_actividad_pandas_caba.ipynb)

Cada grupo debe completar la plantilla con:

- nombre del dataset elegido;
- explicación de qué representa cada fila;
- exploración inicial del dataset;
- dos o tres hipótesis;
- código usado para verificar cada hipótesis;
- conclusiones.

---

## Cómo formular hipótesis

Una buena hipótesis debe poder responderse usando columnas del dataset.

Estructura recomendada:

```text
Hipótesis:
Creemos que...

Columnas necesarias:
Usaremos las columnas...

Método:
Vamos a usar...

Resultado esperado:
Esperamos encontrar...

Conclusión:
Los datos muestran que...
```

Ejemplos de hipótesis válidas:

- “La cantidad de registros no está distribuida uniformemente entre comunas.”
- “La categoría más frecuente concentra más del 50% de los registros.”
- “El promedio de una variable numérica cambia según el barrio o la comuna.”
- “La cantidad de registros varía según el año o el mes.”
- “Hay barrios o comunas que aparecen mucho más que otros.”

---

## Qué hipótesis evitar

Eviten hipótesis demasiado simples, por ejemplo:

- “El dataset tiene muchas filas.”
- “Existe una columna llamada comuna.”
- “Hay datos de CABA.”
- “Hay valores distintos en una columna.”

También eviten hipótesis demasiado difíciles o causales, por ejemplo:

- “Este fenómeno ocurre porque...”
- “Este dataset demuestra que una política pública fue exitosa.”
- “Este barrio es mejor que otro.”
- “La causa de los accidentes es...”
- “La calidad de vida depende de...”

En esta actividad trabajamos principalmente con análisis descriptivo. Podemos decir qué muestran los datos, pero no siempre podemos explicar por qué ocurre.

---

## Operaciones útiles de pandas

```python
df.head()
df.info()
df.shape
df.columns
df.describe()
df.nunique()
df.isna().sum()
df["columna"].value_counts()
df.groupby("columna").size()
df.groupby("grupo")["valor"].mean()
df.sort_values("columna")
df[df["columna"] > valor]
```

---

## Presentación grupal

Cada grupo debe preparar una presentación oral de aproximadamente **5 minutos** para la próxima clase.

La presentación debe incluir:

1. Nombre del dataset elegido.
2. Fuente del dataset.
3. Qué representa cada fila.
4. Columnas principales.
5. Hipótesis planteadas.
6. Operaciones de pandas utilizadas.
7. Resultados obtenidos.
8. Conclusión: se cumple, no se cumple o no se puede verificar.
9. Limitaciones del análisis.

No hace falta que la hipótesis se cumpla. Una hipótesis que no se cumple puede estar perfectamente trabajada.

---

## Criterios de evaluación

| Criterio | Qué se espera |
|---|---|
| Dataset | Se entiende qué representa cada fila y qué columnas son relevantes. |
| Hipótesis | Son verificables, no triviales y no imposibles. |
| Uso de pandas | Se usan operaciones adecuadas como filtros, conteos, agrupamientos, promedios u ordenamientos. |
| Interpretación | Las conclusiones no exageran lo que los datos permiten afirmar. |
| Presentación | El grupo explica dataset, método, resultado y conclusión con claridad. |

---

## Entrega

Cada grupo deberá entregar o compartir:

- el notebook completo;
- el archivo de datos utilizado o el enlace al dataset;
- la presentación de 5 minutos.
