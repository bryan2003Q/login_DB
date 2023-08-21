import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de contactos")
root.geometry("600x400")

# Crear el menú
menu = tk.Menu(root)
root.config(menu=menu)

# Crear el submenú Archivo
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Nuevo contacto")
file_menu.add_command(label="Abrir contacto")
file_menu.add_command(label="Guardar contacto")
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.destroy)
menu.add_cascade(label="Archivo", menu=file_menu)

# Crear el submenú Editar
edit_menu = tk.Menu(menu, tearoff=0)
edit_menu.add_command(label="Cortar")
edit_menu.add_command(label="Copiar")
edit_menu.add_command(label="Pegar")
edit_menu.add_separator()
edit_menu.add_command(label="Buscar")
menu.add_cascade(label="Editar", menu=edit_menu)

# Crear el submenú Opciones
options_menu = tk.Menu(menu, tearoff=0)
options_menu.add_command(label="Tema")
options_menu.add_command(label="Firma")
options_menu.add_command(label="Reglas")
menu.add_cascade(label="Opciones", menu=options_menu)

# Crear la barra de herramientas
toolbar = ttk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Crear los botones de la barra de herramientas
new_button = ttk.Button(toolbar, text="Nuevo")
new_button.pack(side=tk.LEFT, padx=2, pady=2)
save_button = ttk.Button(toolbar, text="Guardar")
save_button.pack(side=tk.LEFT, padx=2, pady=2)
delete_button = ttk.Button(toolbar, text="Eliminar")
delete_button.pack(side=tk.LEFT, padx=2, pady=2)

# Crear el panel principal con los campos para ingresar los datos del contacto
main_panel = ttk.Frame(root)
main_panel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Crear las etiquetas y las entradas para los datos del contacto
name_label = ttk.Label(main_panel, text="Nombre:")
name_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
name_entry = ttk.Entry(main_panel)
name_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=10)

email_label = ttk.Label(main_panel, text="Correo electrónico:")
email_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
email_entry = ttk.Entry(main_panel)
email_entry.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=10)

phone_label = ttk.Label(main_panel, text="Teléfono:")
phone_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
phone_entry = ttk.Entry(main_panel)
phone_entry.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=10)

address_label = ttk.Label(main_panel, text="Dirección:")
address_label.grid(row=3, column=0, sticky=tk.N, padx=10, pady=10)
address_text = tk.Text(main_panel)
address_text.grid(row=3, column=1, sticky=tk.NSEW, padx=10, pady=10)

# Hacer que la columna 1 se expanda con la ventana
main_panel.columnconfigure(1, weight=1)

# Iniciar el bucle principal de la aplicación
root.mainloop()
