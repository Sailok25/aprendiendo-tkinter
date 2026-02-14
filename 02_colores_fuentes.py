import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejercicio 2: Colores y Fuentes")
ventana.geometry("600x400")

lbl_con_color_fondo = ttk.Label(ventana, text='Un texto con color de fondo!', background='green', foreground='white')
lbl_con_color_fondo.pack()

lbl_con_fuente = tk.Label(ventana, text='Un texto con una fuente diferente!', font=('Arial'))
lbl_con_fuente.pack()

lbl_con_tamano = tk.Label(ventana, text='Un texto con un tamaño de fuente diferente!', font=('Courier', 15))
lbl_con_tamano.pack()

lbl_con_fuente_color_tamano = tk.Label(ventana, text='Soy un texto con fondo, fuente y tamaño personalizados!', background='blue', foreground='orange', font=('Times New Roman', 15))
lbl_con_fuente_color_tamano.pack()

ventana.mainloop()