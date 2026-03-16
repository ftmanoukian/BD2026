import pandas as pd
datos = pd.read_csv("notas_examen.csv")
print(datos.drop(columns=['Matemática','Historia','Física']))