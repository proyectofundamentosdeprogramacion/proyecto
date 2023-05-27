import pandas as pd
from tkinter import *
from pandastable import Table, TableModel

# Cargar los datos del archivo Excel en un DataFrame
ruta = r'C:\Users\USUARIO\Desktop\Material de estudio\Fundamentos de Programacion\proyecto\All_Book_Data.csv'
df = pd.read_csv(ruta)

# Función para realizar la búsqueda de libros
def buscar_libro():
    query = entrada_busqueda.get()
    resultado = df[df['book_name'].str.contains(query, case=False)]
    tabla_modelo.setDataFrame(resultado)

# Crear la ventana principal
ventana = Tk()
ventana.title('Biblioteca de Libros')
ventana.geometry('800x600')

# Crear un marco para contener la tabla de datos
marco_tabla = Frame(ventana)
marco_tabla.pack(fill=BOTH, expand=1)

# Crear una instancia de la clase TableModel con los datos del DataFrame
tabla_modelo = TableModel(dataframe=df)

# Crear una instancia de la clase Table con la tabla de datos
tabla_datos = Table(marco_tabla, model=tabla_modelo)
tabla_datos.show()

# Crear un campo de entrada y un botón para buscar libros
marco_busqueda = Frame(ventana)
marco_busqueda.pack(pady=10)

label_busqueda = Label(marco_busqueda, text='Buscar libro:')
label_busqueda.pack(side=LEFT)

entrada_busqueda = Entry(marco_busqueda, width=30)
entrada_busqueda.pack(side=LEFT)

boton_buscar = Button(marco_busqueda, text='Buscar', command=buscar_libro)
boton_buscar.pack(side=LEFT)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
