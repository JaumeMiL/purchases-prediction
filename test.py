import pandas as pd

df = pd.read_excel('../assets/consumo_material_clean.xlsx')
# Suponiendo que 'df' es tu DataFrame y 'codigo' es el nombre de la columna
n_total_rows = len(df)
n_unique_values = df['PRECIO'].nunique()
n_unique_values_2 = df['PRODUCTO'].nunique()

print(n_unique_values)
print(n_unique_values_2)

# Comprobar si todos los valores son únicos
all_unique = n_unique_values_2 == n_unique_values

print("¿Todos los valores en la columna 'codigo' son únicos?:", all_unique)
