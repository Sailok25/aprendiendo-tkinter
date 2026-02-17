import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 5: Layout Pack - Parte 2")
ventana.geometry("600x400")

# Fill con TOP
l1 = tk.Label(ventana, text="Fill=X", bg="red", fg="white")
l2 = tk.Label(ventana, text="Fill=NONE", bg="green", fg="white")
l1.pack(side=tk.TOP, fill=tk.X)
l2.pack(side=tk.TOP, fill=tk.NONE)

# Fill con LEFT
l3 = tk.Label(ventana, text="Fill=Y", bg="blue", fg="white")
l4 = tk.Label(ventana, text="Fill=BOTH", bg="purple", fg="white")
l3.pack(side=tk.LEFT, fill=tk.Y)
l4.pack(side=tk.LEFT, fill=tk.BOTH)

ventana.mainloop()