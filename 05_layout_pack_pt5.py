import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejercicio 5: Layout Pack - Parte 5')
ventana.geometry('600x400')

box1 = tk.Label(ventana, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, anchor=tk.E,  expand=True)
box2 = tk.Label(ventana, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, anchor=tk.W, expand=True)


ventana.mainloop()