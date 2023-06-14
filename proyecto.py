from tkinter import *
import tkinter as tk
import database
import random
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from tkinter import Toplevel

# funciones
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

def abrir_busqueda_personalizada():
    global entry_busqueda, entry_precio_min, entry_precio_max, entry_lenguaje, entry_fecha_lanzamiento
    global lista_resultados
    # ventana principal
    ventana_principal = Toplevel()
    ventana_principal.title("Biblioteca")
    ventana_principal.geometry("395x510")
    ventana_principal.resizable(0, 0)
    ventana_principal.config(bg="deep sky blue")

    # frame titulo
    frame_titulo_principal = Frame(ventana_principal)
    frame_titulo_principal.config(bg="aquamarine2", width=375, height=60)
    frame_titulo_principal.place(x=10, y=10)

    lb_titulo = Label(frame_titulo_principal, text="F u n d a m e n t a l s   o f    C o d e")
    lb_titulo.config(bg="aquamarine2", fg="black", font=("MS Serif", 19))
    lb_titulo.place(relx=0.5, rely=0.5, anchor=CENTER)

    # frame entrada de datos
    frame_entrada_datos = Frame(ventana_principal)
    frame_entrada_datos.config(bg="aquamarine2", width=430, height=610)
    frame_entrada_datos.place(x=10, y=80)

    # Agregar el contenido de la ventana de búsqueda personalizada
    etiqueta = Label(frame_entrada_datos, bg="aquamarine2", text="Ventana de Búsqueda Personalizada")
    etiqueta.config(font=("MS Serif", 16))
    etiqueta.grid(row=0, column=0, columnspan=2, pady=10)

    # Etiqueta y Entry para ingresar la búsqueda
    etiqueta_busqueda = Label(frame_entrada_datos, bg="aquamarine2", text="Buscar libro:")
    etiqueta_busqueda.grid(row=1, column=0, sticky=W, padx=10)

    entry_busqueda = Entry(frame_entrada_datos, width=30)
    entry_busqueda.grid(row=1, column=1, padx=10)

    # Etiqueta y Entry para el precio mínimo
    etiqueta_precio_min = Label(frame_entrada_datos, bg="aquamarine2", text="Precio mínimo:")
    etiqueta_precio_min.grid(row=2, column=0, sticky=W, padx=10)

    entry_precio_min = Entry(frame_entrada_datos, width=10)
    entry_precio_min.grid(row=2, column=1, padx=10)

    # Etiqueta y Entry para el precio máximo
    etiqueta_precio_max = Label(frame_entrada_datos, bg="aquamarine2", text="Precio máximo:")
    etiqueta_precio_max.grid(row=3, column=0, sticky=W, padx=10)

    entry_precio_max = Entry(frame_entrada_datos, width=10)
    entry_precio_max.grid(row=3, column=1, padx=10)

    # Etiqueta y Entry para el lenguaje de programación
    etiqueta_lenguaje = Label(frame_entrada_datos, bg="aquamarine2", text="Lenguaje de programación:")
    etiqueta_lenguaje.grid(row=4, column=0, sticky=W, padx=10)

    entry_lenguaje = Entry(frame_entrada_datos, width=30)
    entry_lenguaje.grid(row=4, column=1, padx=10)

    # Etiqueta y Entry para la fecha de lanzamiento
    etiqueta_fecha_lanzamiento = Label(frame_entrada_datos, bg="aquamarine2", text="Fecha de lanzamiento:")
    etiqueta_fecha_lanzamiento.grid(row=5, column=0, sticky=W, padx=10)

    entry_fecha_lanzamiento = Entry(frame_entrada_datos, width=15)
    entry_fecha_lanzamiento.grid(row=5, column=1, padx=10)

    # Botón para realizar la búsqueda
    boton_buscar = Button(frame_entrada_datos, text="Buscar", command=buscar_libro)
    boton_buscar.grid(row=6, column=0, columnspan=2, pady=10)

    # frame salida de datos
    frame_salida_datos = Frame(ventana_principal)
    frame_salida_datos.config(bg="aquamarine2", width=430, height=610)
    frame_salida_datos.place(x=10, y=290)

    # ListBox para mostrar los resultados de la búsqueda
    lista_resultados = Listbox(frame_salida_datos, bg="aquamarine2", width=62)
    lista_resultados.pack(fill=BOTH, expand=True)

    # Scrollbar para el ListBox de resultados de la búsqueda
    scrollbar_resultados = Scrollbar(frame_salida_datos)
    scrollbar_resultados.pack(side=RIGHT, fill=Y)

    # Asociar el Scrollbar con el ListBox de resultados de la búsqueda
    lista_resultados.config(yscrollcommand=scrollbar_resultados.set)
    scrollbar_resultados.config(command=lista_resultados.yview)

    # Función para mostrar el detalle del libro seleccionado de la búsqueda
    lista_resultados.bind('<<ListboxSelect>>', mostrar_detalle)

def abrir_busqueda_recomendada():
    global lista_libros_aleatorios
    # Crear la ventana principal
    ventana = Toplevel()
    ventana.title("Libros Sugerencia")
    ventana.resizable(0, 0)
    ventana.config(bg="deep sky blue")
    ventana.geometry("500x500")

    # Label para mostrar los libros aleatorios
    etiqueta_libros_aleatorios = Label(ventana, text="Libros Sugeridos:")
    etiqueta_libros_aleatorios.config(bg="aquamarine2", fg="black", font=("MS Serif", 19))
    etiqueta_libros_aleatorios.place(x=165, y=10)

    # ListBox para mostrar los libros aleatorios
    lista_libros_aleatorios = Listbox(ventana, width=50)
    lista_libros_aleatorios.config(bg="aquamarine2", fg="black")
    lista_libros_aleatorios.place(x=100, y=60)

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
    boton_libros_aleatorios.config(bg="aquamarine2", fg="black", font=("MS Serif", 19))
    boton_libros_aleatorios.place(x=180, y=250)


# ventana bienvenida
ventana_bienvenida = Tk()
ventana_bienvenida.title("Fundamentals of Code")
ventana_bienvenida.geometry("395x510")
ventana_bienvenida.resizable(0, 0)
ventana_bienvenida.config(bg="deep sky blue")

# frame titulo
frame_titulo_principal = Frame(ventana_bienvenida)
frame_titulo_principal.config(bg="aquamarine2", width=375, height=60)
frame_titulo_principal.place(x=10, y=10)

lb_titulo = Label(frame_titulo_principal, text="F u n d a m e n t a l s   o f    C o d e")
lb_titulo.config(bg="aquamarine2", fg="black", font=("MS Serif", 19))
lb_titulo.place(relx=0.5, rely=0.5, anchor=CENTER)

# texto de bienvenida
frame_texto1 = Frame(ventana_bienvenida)
frame_texto1.config(bg="aquamarine2", width=375, height=210)
frame_texto1.place(x=10, y=80)

# Crear el Label de bienvenida
lb_bienvenida = Label(frame_texto1, text="¡Bienvenido a nuestra aplicación de recomendación de \n"
                      "libros de programación!\n\n"
                                                "¿Estás buscando libros de programación específicos o prefieres que te recomendemos algunos basados en tus intereses?"
                                                "¡Explora nuestra biblioteca y elige entre una búsqueda personalizada o nuestras recomendaciones!",
                        bg="aquamarine2", fg="black", font=("Arial", 11), wraplength=400)

# Ubicar el Label en la ventana o frame correspondiente
lb_bienvenida.place(relx=0.5, rely=0.5, anchor=CENTER)

# Botón para busqueda personalizada
boton_ventana_personalizada = Button(ventana_bienvenida, text="Busqueda Personalizada", command=abrir_busqueda_personalizada)
boton_ventana_personalizada.config(bg="aquamarine2", fg="black", font=("MS Serif", 19))
boton_ventana_personalizada.place(x=70, y= 320)

# Botón para busqueda recomendada
boton_ventana_recomendada = Button(ventana_bienvenida, text="Busqueda Recomendada", command=abrir_busqueda_recomendada)
boton_ventana_recomendada.config(bg="aquamarine2", fg="black", font=("MS Serif", 19))
boton_ventana_recomendada.place(x=70, y= 390)

# correr programa
ventana_bienvenida.mainloop()
