import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de correo electrónico")
root.geometry("800x600")

# Crear el menú
menu = tk.Menu(root)
root.config(menu=menu)

# Crear el submenú Archivo
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Nuevo correo")
file_menu.add_command(label="Abrir correo")
file_menu.add_command(label="Guardar correo")
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
update_button = ttk.Button(toolbar, text="Actualizar")
update_button.pack(side=tk.LEFT, padx=2, pady=2)
search_button = ttk.Button(toolbar, text="Buscar")
search_button.pack(side=tk.LEFT, padx=2, pady=2)

# Crear el panel izquierdo con la lista de carpetas
left_panel = ttk.Frame(root)
left_panel.pack(side=tk.LEFT, fill=tk.Y)

# Crear el widget Treeview para la lista de carpetas
folder_tree = ttk.Treeview(left_panel)
folder_tree.pack(side=tk.LEFT, fill=tk.Y)

# Añadir algunas carpetas al árbol
folder_tree.insert("", "end", text="Bandeja de entrada", tags=("inbox"))
folder_tree.insert("", "end", text="Enviados", tags=("sent"))
folder_tree.insert("", "end", text="Borradores", tags=("drafts"))
folder_tree.insert("", "end", text="Spam", tags=("spam"))

# Crear el panel derecho con el panel de mensajes y el panel de vista previa
right_panel = ttk.PanedWindow(root, orient=tk.VERTICAL)
right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Crear el panel de mensajes con una lista de correos electrónicos
message_panel = ttk.Frame(right_panel)
message_panel.pack(fill=tk.BOTH, expand=True)
right_panel.add(message_panel)

# Crear el widget Listbox para la lista de correos electrónicos
message_list = tk.Listbox(message_panel)
message_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Añadir algunos correos electrónicos a la lista
message_list.insert(tk.END, "Juan Pérez <juan.perez@example.com> | Asunto: Hola | Fecha: 20/08/2023")
message_list.insert(tk.END, "María García <maria.garcia@example.com> | Asunto: Reunión | Fecha: 19/08/2023")
message_list.insert(tk.END, "Luis Rodríguez <luis.rodriguez@example.com> | Asunto: Informe | Fecha: 18/08/2023")

# Crear el panel de vista previa con una etiqueta que muestra el contenido del correo electrónico seleccionado
preview_panel = ttk.Frame(right_panel)
preview_panel.pack(fill=tk.BOTH, expand=True)
right_panel.add(preview_panel)

# Crear el widget Label para el contenido del correo electrónico
email_content = tk.Label(preview_panel, text="Aquí se mostrará el contenido del correo electrónico seleccionado.")
email_content.pack(fill=tk.BOTH, expand=True)

# Iniciar el bucle principal de la aplicación
root.mainloop()