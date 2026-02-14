import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejercicio 2: Colores y Fuentes")
ventana.geometry("600x400")

lbl_con_color_fondo = ttk.Label(ventana, text='Un texto con color de fondo!', background='green', foreground='white')
lbl_con_color_fondo.pack()

lbl_con_fuente = tk.Label(ventana, text='Un texto con una fuente y tamaño diferente!', font=('Courier', 12))
lbl_con_fuente.pack()

ventana.mainloop()