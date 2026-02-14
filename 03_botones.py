import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejercicio 3: Botones")
ventana.geometry("600x400")

btn = tk.Button(ventana, text="Soy un boton que no hace nada")
btn.pack()

btn_terminal = tk.Button(ventana, text="Soy un boton que imprime en terminal", command=lambda: print("¡Hola!"))
btn_terminal.pack()

ventana.mainloop()