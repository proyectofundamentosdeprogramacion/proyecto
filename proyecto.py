from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from tkinter import Toplevel

#funciones


#ventana principal
ventana_principal = Tk()
ventana_principal.title("Biblioteca")
ventana_principal.geometry("900x700")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="deep sky blue")

#frame titulo
frame_titulo_principal = Frame(ventana_principal)
frame_titulo_principal.config(bg="aquamarine2", width=880, height=60)
frame_titulo_principal.place(x=10, y=10)

lb_titulo = Label(frame_titulo_principal, text ="F u n d a m e n t a l s    o f    C o d e")
lb_titulo.config(bg="aquamarine2", fg="black", font=("MS Serif", 22))
lb_titulo.place(relx=0.5, rely=0.5, anchor=CENTER)


#correr programa
ventana_principal.mainloop()