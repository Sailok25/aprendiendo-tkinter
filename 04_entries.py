import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejercicio 4: Entries")
ventana.geometry("600x400")

etiqueta_nombre = ttk.Label(ventana, text="Introduce tu nombre:", font=("Arial", 14))
etiqueta_nombre.pack(pady=1)
introducir_nombre = ttk.Entry(ventana)
introducir_nombre.focus()
introducir_nombre.pack(pady=5)

etiqueta_email = ttk.Label(ventana, text="Introduce tu email:", font=("Arial", 14))
etiqueta_email.pack(pady=1)
introducir_email = ttk.Entry(ventana)
introducir_email.pack()

etiqueta_contrasena = ttk.Label(ventana, text="Introduce tu contraseña:", font=("Arial", 14))
etiqueta_contrasena.pack(pady=1)
visualizar_contrasena = tk.StringVar()
introducir_contrasena = ttk.Entry(ventana, show="*", textvariable=visualizar_contrasena)
introducir_contrasena.pack()

output_contrasena = ttk.Label(ventana)
output_contrasena.pack(pady=1)
visualizar_contrasena.trace_add("write", lambda *args: output_contrasena.config(text=visualizar_contrasena.get()))

ventana.mainloop()