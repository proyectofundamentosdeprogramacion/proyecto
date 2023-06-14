from tkinter import *
from tkinter import messagebox
import database
import random


def buscar_libro():
    # Obtener los valores de los filtros
    texto_busqueda = entry_busqueda.get()
    precio_min = entry_precio_min.get()
    precio_max = entry_precio_max.get()
    lenguaje = entry_lenguaje.get()
    fecha_lanzamiento = entry_fecha_lanzamiento.get()

    # Validar que al menos uno de los campos esté lleno
    if not texto_busqueda and not precio_min and not precio_max and not lenguaje and not fecha_lanzamiento:
        messagebox.showerror("Error", "Debes ingresar al menos un criterio de búsqueda.")
        return

    # Validar que los campos de precio solo contengan números
    if precio_min and not precio_min.isdigit():
        messagebox.showerror("Error", "El precio mínimo debe ser un número.")
        return

    if precio_max and not precio_max.isdigit():
        messagebox.showerror("Error", "El precio máximo debe ser un número.")
        return

    # Convertir los valores de precio a flotantes si están llenos
    if precio_min:
        precio_min = float(precio_min)
    else:
        precio_min = float('-inf')

    if precio_max:
        precio_max = float(precio_max)
    else:
        precio_max = float('inf')

    # Buscar el libro en la base de datos
    resultados = []
    for data in database.libros:
        if (texto_busqueda.lower() in data['book_name'].lower() or
                texto_busqueda.lower() in data['author'].lower()):
            # Validar el rango de precio
            precio = float(str(data['price']).replace('$', ''))
            if precio_min <= precio <= precio_max:
                # Validar el lenguaje de programación
                if lenguaje and 'programming_language' in data and lenguaje.lower() != data['programming_language'].lower():
                    continue

                # Validar la fecha de lanzamiento
                if fecha_lanzamiento and 'release_date' in data and fecha_lanzamiento != data['release_date']:
                    continue

                resultados.append(data)

    # Mostrar los resultados
    mostrar_resultados(resultados)


def mostrar_resultados(resultados):
    # Borrar contenido anterior en el ListBox
    lista_resultados.delete(0, END)

    # Mostrar los resultados en el ListBox
    for libro in resultados:
        lista_resultados.insert(END, f"{libro['book_name']} - {libro['author']}")


def mostrar_detalle(event):
    # Obtener el widget que generó el evento
    widget = event.widget

    # Obtener el índice del libro seleccionado
    indice_seleccionado = widget.curselection()
    if indice_seleccionado:
        indice = indice_seleccionado[0]

        # Obtener el libro correspondiente
        libro = widget.get(indice)

        # Buscar el libro en la base de datos
        for data in database.libros:
            if libro.startswith(data['book_name']):
                # Mostrar el detalle del libro en un messagebox
                messagebox.showinfo("Detalle del Libro",
                                    f"Nombre: {data['book_name']}\n"
                                    f"Autor: {data['author']}\n"
                                    f"Páginas: {data.get('page', 'N/A')}\n"
                                    f"Fecha de lanzamiento: {data.get('release_date', 'N/A')}\n"
                                    f"Descripción: {data.get('short_description', 'N/A')}\n"
                                    f"Precio: {data.get('price', 'N/A')}\n"
                                    f"Lenguaje de programación: {data.get('programming_language', 'N/A')}\n"
                                    f"Concepto: {data.get('concept', 'N/A')}\n"
                                    f"Herramienta: {data.get('tool', 'N/A')}")
                break


def mostrar_libros_aleatorios():
    # Generar 3 índices aleatorios
    indices_aleatorios = random.sample(range(len(database.libros)), 3)

    # Obtener los libros aleatorios correspondientes a los índices
    libros_aleatorios = [database.libros[i] for i in indices_aleatorios]

    # Borrar contenido anterior en el ListBox de libros aleatorios
    lista_libros_aleatorios.delete(0, END)

    # Mostrar los libros aleatorios en el ListBox
    for libro in libros_aleatorios:
        lista_libros_aleatorios.insert(END, f"{libro['book_name']} - {libro['author']}")


def abrir_ventana_busqueda_personalizada():
    global entry_busqueda, entry_precio_min, entry_precio_max, entry_lenguaje, entry_fecha_lanzamiento
    global lista_resultados, lista_libros_aleatorios, ventana_busqueda_personalizada
    # Crear la ventana de búsqueda personalizada
    ventana_busqueda_personalizada = Toplevel()
    ventana_busqueda_personalizada.title("Búsqueda Personalizada")
    ventana_busqueda_personalizada.geometry("400x600")

    # Agregar el contenido de la ventana de búsqueda personalizada
    etiqueta = Label(ventana_busqueda_personalizada, text="Ventana de Búsqueda Personalizada")
    etiqueta.pack()

    # Etiqueta y Entry para ingresar la búsqueda
    etiqueta_busqueda = Label(ventana_busqueda_personalizada, text="Buscar libro:")
    etiqueta_busqueda.pack()

    entry_busqueda = Entry(ventana_busqueda_personalizada, width=30)
    entry_busqueda.pack()

    # Etiqueta y Entry para el precio mínimo
    etiqueta_precio_min = Label(ventana_busqueda_personalizada, text="Precio mínimo:")
    etiqueta_precio_min.pack()

    entry_precio_min = Entry(ventana_busqueda_personalizada, width=10)
    entry_precio_min.pack()

    # Etiqueta y Entry para el precio máximo
    etiqueta_precio_max = Label(ventana_busqueda_personalizada, text="Precio máximo:")
    etiqueta_precio_max.pack()

    entry_precio_max = Entry(ventana_busqueda_personalizada, width=10)
    entry_precio_max.pack()

    # Etiqueta y Entry para el lenguaje de programación
    etiqueta_lenguaje = Label(ventana_busqueda_personalizada, text="Lenguaje de programación:")
    etiqueta_lenguaje.pack()

    entry_lenguaje = Entry(ventana_busqueda_personalizada, width=30)
    entry_lenguaje.pack()

    # Etiqueta y Entry para la fecha de lanzamiento
    etiqueta_fecha_lanzamiento = Label(ventana_busqueda_personalizada, text="Fecha de lanzamiento:")
    etiqueta_fecha_lanzamiento.pack()

    entry_fecha_lanzamiento = Entry(ventana_busqueda_personalizada, width=15)
    entry_fecha_lanzamiento.pack()

    # Botón para realizar la búsqueda
    boton_buscar = Button(ventana_busqueda_personalizada, text="Buscar", command=buscar_libro)
    boton_buscar.pack()

    # ListBox para mostrar los resultados de la búsqueda
    lista_resultados = Listbox(ventana_busqueda_personalizada, width=50)
    lista_resultados.pack()

    # Scrollbar para el ListBox de resultados de la búsqueda
    scrollbar_resultados = Scrollbar(ventana_busqueda_personalizada)
    scrollbar_resultados.pack(side=RIGHT, fill=Y)

    # Asociar el Scrollbar con el ListBox de resultados de la búsqueda
    lista_resultados.config(yscrollcommand=scrollbar_resultados.set)
    scrollbar_resultados.config(command=lista_resultados.yview)

    # Función para mostrar el detalle del libro seleccionado de la búsqueda
    lista_resultados.bind('<<ListboxSelect>>', mostrar_detalle)

    # Cerrar la ventana de búsqueda personalizada al hacer clic en el botón "Cerrar"
    boton_cerrar = Button(ventana_busqueda_personalizada, text="Cerrar", command=ventana_busqueda_personalizada.destroy)
    boton_cerrar.pack()


# Crear la ventana principal
ventana = Tk()
ventana.title("Búsqueda de Libros")
ventana.geometry("500x500")

# Label para mostrar los libros aleatorios
etiqueta_libros_aleatorios = Label(ventana, text="Libros Sugeridos:")
etiqueta_libros_aleatorios.pack()

# ListBox para mostrar los libros aleatorios
lista_libros_aleatorios = Listbox(ventana, width=50)
lista_libros_aleatorios.pack()

# Scrollbar para el ListBox de libros aleatorios
scrollbar_libros_aleatorios = Scrollbar(ventana)
scrollbar_libros_aleatorios.pack(side=RIGHT, fill=Y)

# Asociar el Scrollbar con el ListBox de libros aleatorios
lista_libros_aleatorios.config(yscrollcommand=scrollbar_libros_aleatorios.set)
scrollbar_libros_aleatorios.config(command=lista_libros_aleatorios.yview)

# Función para mostrar el detalle del libro seleccionado de los libros aleatorios
lista_libros_aleatorios.bind('<<ListboxSelect>>', mostrar_detalle)

# Botón para mostrar libros aleatorios
boton_libros_aleatorios = Button(ventana, text="Sugerir libros", command=mostrar_libros_aleatorios)
boton_libros_aleatorios.pack()

# Botón para abrir la ventana de búsqueda personalizada
boton_busqueda_personalizada = Button(ventana, text="Búsqueda Personalizada", command=abrir_ventana_busqueda_personalizada)
boton_busqueda_personalizada.pack()

# Ejecutar la ventana principal
ventana.mainloop()
