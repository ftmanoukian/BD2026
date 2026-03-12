import pandas as pd
datos = pd.read_csv("clase2/notas_examen.csv")
#print(datos.drop(columns=["Alumno"]).mean().mean())
print(datos.iloc[0].drop("Alumno").mean())