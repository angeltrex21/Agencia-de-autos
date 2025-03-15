import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Definición de las rutas de los archivos
ruta_archivo_1 = 'C:/Users/jacin/OneDrive/Documentos/base de datos de escuela/INVESCOBEDO.txt'
ruta_archivo_2 = 'C:/Users/jacin/OneDrive/Documentos/base de datos de escuela/INVAPODACA.txt'
ruta_archivo_3 = 'C:/Users/jacin/OneDrive/Documentos/base de datos de escuela/INVMONTERREY.txt'
ruta_archivo_4 = 'C:/Users/jacin/OneDrive/Documentos/base de datos de escuela/INVSANNICOLAS.txt'

# Creación de los DataFrames utilizando las rutas definidas
df_1 = pd.read_csv(ruta_archivo_1, delimiter='|')  
df_2 = pd.read_csv(ruta_archivo_2, delimiter='|')  
df_3 = pd.read_csv(ruta_archivo_3, delimiter='|')
df_4 = pd.read_csv(ruta_archivo_4, delimiter='|')

# Concatenación de los DataFrames en uno solo
df_completo = pd.concat([df_1, df_2, df_3, df_4], ignore_index=True)
df_completo.dtypes
print("",df_completo.dtypes)
df_completo.info
print("",df_completo.info)

#cantidad de unidades
cantiad_unidades= len(df_completo)
print("cantiad de unidades:",cantiad_unidades)

#cantidad de unidades disponibles
cantiad_unidades_disponibles = df_completo[df_completo['Estado']=='DISPONIBLE'].shape[0]
print("Cantidad total de unidades disponibles:",cantiad_unidades_disponibles)

#Cantidad de unidades no dsiponibles
cantiad_no_disponibles = df_completo[df_completo['Estado']=='NODISPONIBLE'].shape[0]
print("Cantidad total de unidades no disponibles:",cantiad_no_disponibles)

#Total de costo de las uniades 
total_costo_unidades=df_completo['CostoActual'].sum()
print("Csoto total de las unidades=",total_costo_unidades)

#Costo mas alto
costo_alto=df_completo['CostoActual'].max()
print("EL costo mas alto es:",costo_alto)

#Costo mas bajo
costo_bajo=df_completo['CostoActual'].min()
print("EL costo mas alto es:",costo_bajo)

# Gráfica 1: Inventario por cantidad de unidades por modelo
plt.figure(figsize=(12, 6))
sns.countplot(data=df_completo, x='Modelo', order=df_completo['Modelo'].value_counts().index)
plt.title('Inventario por Cantidad de Unidades por Modelo')
plt.xlabel('Modelo')
plt.ylabel('Cantidad de Unidades')
plt.xticks(rotation=90)
plt.show()

# Gráfica 2: Inventario por cantidad de unidades por marca
plt.figure(figsize=(12, 6))
sns.countplot(data=df_completo, x='Marca', order=df_completo['Marca'].value_counts().index)
plt.title('Inventario por Cantidad de Unidades por Marca')
plt.xlabel('Marca')
plt.ylabel('Cantidad de Unidades')
plt.xticks(rotation=90)
plt.show()

# Gráfica 3: Inventario por costo por modelo
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_completo, x='Modelo', y='CostoActual', order=df_completo['Modelo'].value_counts().index)
plt.title('Inventario por Costo por Modelo')
plt.xlabel('Modelo')
plt.ylabel('Costo Actual')
plt.xticks(rotation=90)
plt.show()

# Gráfica 4: Inventario por costo por marca
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_completo, x='Marca', y='CostoActual', order=df_completo['Marca'].value_counts().index)
plt.title('Inventario por Costo por Marca')
plt.xlabel('Marca')
plt.ylabel('Costo Actual')
plt.xticks(rotation=90)
plt.show()

# Filtrar por Modelo
modelo_filtro ='K3 SEDAN'
df_filtrado=df_completo[df_completo['Modelo']==modelo_filtro]
print(f"datos filtrados por el modelo '{modelo_filtro}':")
print(df_filtrado.head())

# Filtrar por Marca
marca_filtro ='KIA'
df_filtrado2=df_completo[df_completo['Marca']==marca_filtro]
print(f"datos filtrados por el modelo '{marca_filtro}':")
print(df_filtrado2.head())

# Filtrar por Línea


# Filtrar por Versión

version_filtro ='K3 2.0L GT-LINE A/T Sedan'
df_filtrado3=df_completo[df_completo['Version']==version_filtro]
print(f"datos filtrados por version '{version_filtro}':")
print(df_filtrado3.head())

# Filtrar por Ubicación
ubicacion_filtro ='MONTERREY'
df_filtrado4=df_completo[df_completo['Ubicacion']==ubicacion_filtro]
print(f"datos filtrados por el ubicacion '{ubicacion_filtro}':")
print(df_filtrado4.head())

# Filtrar por Fecha de Compra
fecha_filtro ='05/06/24'
df_filtrado5=df_completo[df_completo['FechaCompra']==fecha_filtro]
print(f"datos filtrados por el fecha '{fecha_filtro}':")
print(df_filtrado5.head())

