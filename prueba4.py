import pandas as pd
import tkinter as tk
from tkinter import ttk

# Cargar los datos del archivo Excel en un DataFrame
ruta = r'C:\Users\USUARIO\Desktop\Material de estudio\Fundamentos de Programacion\proyecto\All_Book_Data.csv'
df = pd.read_csv(ruta)

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca de Libros")

# Crear un diccionario para almacenar los frames de cada libro
frames_libros = {}

# Función para agregar un nuevo libro a la interfaz
def agregar_libro(libro):
    # Crear un nuevo frame para el libro
    frame_libro = ttk.Frame(ventana, padding=10)
    frame_libro.pack()

    # Crear y mostrar los campos de información del libro en el frame correspondiente
    etiqueta_titulo = ttk.Label(frame_libro, text="Título: " + str(libro["book_name"]))
    etiqueta_titulo.pack()

    etiqueta_autor = ttk.Label(frame_libro, text="Autor: " + str(libro["author_name"]))
    etiqueta_autor.pack()

    etiqueta_descripcion = ttk.Label(frame_libro, text="Descripción: " + str(libro["description"]))
    etiqueta_descripcion.pack()

    etiqueta_precio = ttk.Label(frame_libro, text="Precio: $" + str(libro["price"]))
    etiqueta_precio.pack()

    # Agregar el frame del libro al diccionario
    frames_libros[libro["book_name"]] = frame_libro

# Agregar los libros del DataFrame a la interfaz
for index, row in df.iterrows():
    libro = {
        "book_name": row["book_name"],
        "author_name": row["author"],
        "description": row["short_description"],
        "price": row["price"]
    }
    agregar_libro(libro)

# Función para agregar un nuevo libro a través de una ventana de diálogo
def agregar_libro_dialogo():
    # Aquí puedes mostrar una ventana de diálogo para que el usuario ingrese los datos del nuevo libro
    # Una vez que tengas los datos, puedes crear un diccionario con la estructura de datos y llamar a la función agregar_libro

    # Ejemplo:
    nuevo_libro = {
        "book_name": "Nuevo Libro",
        "author_name": "Autor Desconocido",
        "description": "Descripción del nuevo libro...",
        "price": 19.99
    }

    agregar_libro(nuevo_libro)

# Botón para agregar un nuevo libro
boton_agregar = ttk.Button(ventana, text="Agregar Libro", command=agregar_libro_dialogo)
boton_agregar.pack()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
