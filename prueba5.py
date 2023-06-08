import pandas as pd
import tkinter as tk

# Crear la ventana de Tkinter
ventana = tk.Tk()

# Crear un frame para contener el contenido desplazable
frame = tk.Frame(ventana)
frame.pack(fill='both', expand=True)

# Crear una scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

# Crear un lienzo (canvas) para contener el contenido
canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
canvas.pack(side='left', fill='both', expand=True)

# Asociar la scrollbar con el lienzo
scrollbar.config(command=canvas.yview)

# Configurar el desplazamiento con la rueda del ratón
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * int(event.delta / 120), "units"))

# Crear un frame interior en el lienzo para contener las etiquetas
interior = tk.Frame(canvas)
interior.pack()

# Leer el archivo CSV
df = pd.read_csv('All_Book_Data.csv')

# Crear una lista para almacenar las etiquetas de cada libro
etiquetas_libros = []

# Recorrer cada fila del DataFrame
for index, row in df.iterrows():
    try:
        # Crear etiquetas para mostrar las características del libro
        etiqueta_nombre = tk.Label(interior, text="Nombre: {}".format(row['book_name']))
        etiqueta_imagen = tk.Label(interior, text="Imagen: {}".format(row['book_image']))
        etiqueta_autor = tk.Label(interior, text="Autor: {}".format(row['author']))
        etiqueta_paginas = tk.Label(interior, text="Páginas: {}".format(row['page']))
        etiqueta_fecha = tk.Label(interior, text="Fecha de lanzamiento: {}".format(row['release_date']))
        etiqueta_descripcion = tk.Label(interior, text="Descripción breve: {}".format(row['short_description']))
        etiqueta_precio = tk.Label(interior, text="Precio: {}".format(row['price']))
        etiqueta_lenguaje = tk.Label(interior, text="Lenguaje de programación: {}".format(row['programming_language']))
        etiqueta_concepto = tk.Label(interior, text="Concepto: {}".format(row['concept']))
        etiqueta_herramienta = tk.Label(interior, text="Herramienta: {}".format(row['tool']))

        # Agregar las etiquetas a la lista de etiquetas de libros
        etiquetas_libro = [
            etiqueta_nombre,
            etiqueta_imagen,
            etiqueta_autor,
            etiqueta_paginas,
            etiqueta_fecha,
            etiqueta_descripcion,
            etiqueta_precio,
            etiqueta_lenguaje,
            etiqueta_concepto,
            etiqueta_herramienta
        ]
        etiquetas_libros.append(etiquetas_libro)

        # Ubicar las etiquetas en el frame interior
        for etiqueta in etiquetas_libro:
            etiqueta.pack()

        # Agregar un separador entre cada libro
        separador = tk.Label(interior, text="---------------------------------------")
        separador.pack()
    except Exception as e:
        print("Error al procesar un libro:", e)


# Configurar el lienzo para que sea desplazable
canvas.create_window((0, 0), window=interior, anchor='nw')
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Iniciar el bucle principal de la ventana
ventana.mainloop()
