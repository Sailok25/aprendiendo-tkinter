import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejercicio 1: Hola Mundo")
ventana.geometry("600x400")

lbl_hola_mundo = ttk.Label(ventana, text="¡Hola Mundo este es mi primer label!", font=("Arial", 24))
lbl_hola_mundo.pack()

ventana.mainloop()