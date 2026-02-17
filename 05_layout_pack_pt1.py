import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 5: Layout Pack - Parte 1")
ventana.geometry("600x900")

# SIDE (TOP/BOTTOM - LEFT/RIGHT)
l1 = tk.Label(ventana, text="TOP 1", bg="red", fg="white")
l2 = tk.Label(ventana, text="BOTTOM 1", bg="blue", fg="white")
l3 = tk.Label(ventana, text="LEFT 1", bg="red", fg="white")
l4 = tk.Label(ventana, text="RIGHT 1", bg="blue", fg="white")

l1.pack(side=tk.TOP)
l2.pack(side=tk.BOTTOM)
l3.pack(side=tk.LEFT)
l4.pack(side=tk.RIGHT)


#EXPAND (True vs False)
l5 = tk.Label(ventana, text="Expand=True", bg="red", fg="white")
l6 = tk.Label(ventana, text="Expand=False", bg="green", fg="white")
l7 = tk.Label(ventana, text="Expand=True", bg="blue", fg="white")

l5.pack(side=tk.LEFT, expand=True)
l6.pack(side=tk.LEFT, expand=False)
l7.pack(side=tk.LEFT, expand=True)

ventana.mainloop()