import pandas as pd
from tkinter import *
from pandastable import Table, TableModel

# Cargar los datos del archivo Excel en un DataFrame
ruta = r'C:\Users\USUARIO\Desktop\Material de estudio\Fundamentos de Programacion\proyecto\All_Book_Data.csv'
df = pd.read_csv(ruta)

# Crear la ventana principal
ventana = Tk()
ventana.title('Visualización de datos de un archivo Excel con Pandas')
ventana.geometry('800x600')

# Crear un marco para contener la tabla de datos
marco_tabla = Frame(ventana)
marco_tabla.pack(fill=BOTH, expand=1)

# Crear una instancia de la clase TableModel con los datos del DataFrame
tabla_modelo = TableModel(dataframe=df)

# Crear una instancia de la clase Table con la tabla de datos
tabla_datos = Table(marco_tabla, model=tabla_modelo)
tabla_datos.show()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()

