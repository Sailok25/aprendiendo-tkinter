import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejercicio 5: Layout Pack - Parte 4')
ventana.geometry('600x400')

label1 = tk.Label(ventana, text='Pack',bg='red',fg='white')
label2 = tk.Label(ventana, text='Pack',bg='green', fg='white')
label3 = tk.Label(ventana, text='Pack',bg='blue', fg='white')
label4 = tk.Label(ventana, text='Pack',bg='purple', fg='white')
label5 = tk.Label(ventana, text='Pack',bg='red',fg='white')
label6 = tk.Label(ventana, text='Pack',bg='green', fg='white')
label7 = tk.Label(ventana, text='Pack',bg='blue', fg='white')
label8 = tk.Label(ventana, text='Pack',bg='purple', fg='white')

label1.pack(side=tk.TOP, fill=tk.X, pady=10)
label2.pack(side=tk.TOP, fill=tk.X, pady=20)
label3.pack(side=tk.TOP, fill=tk.X ,pady=40)
label4.pack(side=tk.TOP, fill=tk.X, pady=60)
label5.pack(side=tk.LEFT, fill=tk.X, padx=10)
label6.pack(side=tk.LEFT, fill=tk.X, padx=20)
label7.pack(side=tk.LEFT, fill=tk.X ,padx=40)
label8.pack(side=tk.LEFT, fill=tk.X, padx=60)

ventana.mainloop()