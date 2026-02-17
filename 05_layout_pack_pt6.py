import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Ejercicio 5: Layout Pack - Parte 6')
ventana.geometry('600x400')

campos = {}
campos['username_label'] = ttk.Label(ventana, text='Username:')
campos['username'] = ttk.Entry(ventana)
campos['password_label'] = ttk.Label(ventana, text='Password:')
campos['password'] = ttk.Entry(ventana, show="*")

for campo in campos.values():
    campo.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

ttk.Button(text='Login').pack(anchor=tk.W, padx=10, pady=10)

ventana.mainloop()