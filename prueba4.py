import tkinter as tk
from tkinter import ttk

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
    etiqueta_titulo = ttk.Label(frame_libro, text="Título: " + libro["title"])
    etiqueta_titulo.pack()

    etiqueta_autor = ttk.Label(frame_libro, text="Autor: " + libro["author"])
    etiqueta_autor.pack()

    etiqueta_descripcion = ttk.Label(frame_libro, text="Descripción: " + libro["description"])
    etiqueta_descripcion.pack()

    etiqueta_precio = ttk.Label(frame_libro, text="Precio: $" + str(libro["price"]))
    etiqueta_precio.pack()

    # Agregar el frame del libro al diccionario
    frames_libros[libro["title"]] = frame_libro

# Ejemplo de libros
libro1 = {
    "title": "The Elements of Style",
    "author": "William Strunk Jr.",
    "description": "This style manual offers practical advice on improving writing skills...",
    "price": 9.99
}

libro2 = {
    "title": "The Information: A History, a Theory, a Flood",
    "author": "James Gleick",
    "description": "James Gleick, the author of the best sellers Chaos and Genius...",
    "price": 12.99
}

# Agregar los ejemplos de libros a la interfaz
agregar_libro(libro1)
agregar_libro(libro2)

# Función para agregar un nuevo libro a través de una ventana de diálogo
def agregar_libro_dialogo():
    # Aquí puedes mostrar una ventana de diálogo para que el usuario ingrese los datos del nuevo libro
    # Una vez que tengas los datos, puedes crear un diccionario con la estructura de datos y llamar a la función agregar_libro

    # Ejemplo:
    nuevo_libro = {
        "title": "Nuevo Libro",
        "author": "Autor Desconocido",
        "description": "Descripción del nuevo libro...",
        "price": 19.99
    }

    agregar_libro(nuevo_libro)

# Botón para agregar un nuevo libro
boton_agregar = ttk.Button(ventana, text="Agregar Libro", command=agregar_libro_dialogo)
boton_agregar.pack()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
