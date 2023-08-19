import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Interfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Contactos")
        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()                                    
        self.master.geometry("%dx%d+0+0" % (w, h))
        self.master.configure(bg="#CED8F6")  # Color de fondo
        self.contactos = []

     
        frame = tk.Frame(self.master, bg="#CED8F6")
        frame.pack(side="left", anchor="n", padx=10, pady=200)

       
        # Labels y campos de la primera sección
        self.label_instrucciones_nuevo = tk.Label(frame, text='Escriba nombre y email para nuevo contacto', font=("Helvetica", 12))
        self.label_nombre = tk.Label(frame, text='Nombre:', bg="#f2f2f2", font=("Helvetica", 12))
        self.entry_nombre = tk.Entry(frame, font=("Helvetica", 12))
        self.label_email = tk.Label(frame, text='Email:', bg="#f2f2f2", font=("Helvetica", 12))
        self.entry_email = tk.Entry(frame, font=("Helvetica", 12))
        self.boton_nuevo_contacto = ttk.Button(frame, text='Nuevo contacto', command=self.nuevo_contacto,style="TButton" )

      
        self.label_nombre.grid(row=0, column=0, sticky="w", padx=10, pady=(0, 5))
        self.entry_nombre.grid(row=0, column=1, padx=(10))
        self.label_email.grid(row=1, column=0, sticky="w", padx=10, pady=(0, 5))
        self.entry_email.grid(row=1, column=1, padx=(10))
        self.boton_nuevo_contacto.grid(row=2, column=0, columnspan=2, pady=(5, 10))

        # Labels y campos de la segunda sección
        self.label_nombre_modificar = tk.Label(frame, text='Nombre:', bg="#f2f2f2", font=("Helvetica", 12))
        self.entry_nombre_modificar = tk.Entry(frame, font=("Helvetica", 12))
        self.label_email_modificar = tk.Label(frame, text='Email:', bg="#f2f2f2", font=("Helvetica", 12))
        self.entry_email_modificar = tk.Entry(frame, font=("Helvetica", 12))
        self.boton_modificar_contacto = ttk.Button(frame, text='Modificar contacto', command=self.modificar_contacto,style="TButton" )

        self.label_nombre_modificar.grid(row=3, column=0, sticky="w", padx=10, pady=(0, 5))
        self.entry_nombre_modificar.grid(row=3, column=1, padx=(10))
        self.label_email_modificar.grid(row=4, column=0, sticky="w", padx=10, pady=(0, 5))
        self.entry_email_modificar.grid(row=4, column=1, padx=(10))
        self.boton_modificar_contacto.grid(row=5, column=0, columnspan=2, pady=(5, 10))

        self.boton_eliminar_contacto = ttk.Button(frame, text='Eliminar contacto', command=self.eliminar_contacto, style="TButton" )
        self.boton_eliminar_contacto.grid(row=6, column=0, columnspan=2, pady=(5, 10))

        self.treeview_contactos = ttk.Treeview(self.master, columns=("nombre", "email"), selectmode="extended")
        self.treeview_contactos.heading("#0", text="ID")
        self.treeview_contactos.heading("nombre", text="Nombre")
        self.treeview_contactos.heading("email", text="Correo electrónico")
        self.treeview_contactos.column("#0", minwidth=0, width=50, stretch=tk.NO)
        self.treeview_contactos.column("nombre", minwidth=0, width=150, stretch=tk.NO)
        self.treeview_contactos.column("email", minwidth=0, width=350, stretch=tk.NO)
        self.treeview_contactos.pack(anchor="w",padx=300,pady=200)

        self.boton_cerrar_sesion = ttk.Button(frame, text='Cerrar sesión', command=self.cerrar_sesion, style="TButton")
        self.boton_cerrar_sesion.grid(row=7, column=0, columnspan=2, pady=(5, 10))

        self.cargar_contactos()


    def cerrar_sesion(self):
        self.master.destroy()
       
    def nuevo_contacto(self):
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()

        if not nombre or not email:
            messagebox.showinfo("Error", "Por favor, completa los campos de nombre y email.")
            return

        contacto = Contacto(nombre, email)

        self.contactos.append(contacto)
        self.treeview_contactos.insert("", "end", text=str(len(self.contactos)), values=(contacto.nombre, contacto.email))
        self.guardar_contactos()

        self.entry_nombre.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def modificar_contacto(self):
        seleccion = self.treeview_contactos.selection()

        if not seleccion:
            messagebox.showinfo("Error", "Por favor, selecciona un contacto para modificar.")
            return

        indice = int(self.treeview_contactos.item(seleccion[0], "text")) - 1
        contacto = self.contactos[indice]

        nuevo_nombre = self.entry_nombre_modificar.get()
        nuevo_email = self.entry_email_modificar.get()

        if not nuevo_nombre or not nuevo_email:
            messagebox.showinfo("Error", "Por favor, completa los campos de nombre y email.")
            return

        contacto.nombre = nuevo_nombre
        contacto.email = nuevo_email

        self.treeview_contactos.item(seleccion[0], values=(contacto.nombre, contacto.email))
        self.guardar_contactos()

        self.entry_nombre_modificar.delete(0, tk.END)
        self.entry_email_modificar.delete(0, tk.END)

    def eliminar_contacto(self):
        seleccion = self.treeview_contactos.selection()

        if not seleccion:
            messagebox.showinfo("Error", "Por favor, selecciona un contacto para eliminar.")
            return

        indice = int(self.treeview_contactos.item(seleccion[0], "text")) - 1

        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este contacto?")

        if confirmar:
            del self.contactos[indice]
            self.treeview_contactos.delete(seleccion)
            self.guardar_contactos()

    def cargar_contactos(self):
        try:
            with open('contactos.txt', 'r') as archivo:
                lineas = archivo.readlines()
                for i, linea in enumerate(lineas):
                    partes = linea.strip().split(',')
                    contacto = Contacto(partes[0], partes[1])
                    self.contactos.append(contacto)
                    self.treeview_contactos.insert("", "end", text=str(i+1), values=(contacto.nombre, contacto.email))
        except FileNotFoundError:
            pass

    def guardar_contactos(self):
        with open('contactos.txt', 'w') as archivo:
            for contacto in self.contactos:
                archivo.write(f'{contacto.nombre},{contacto.email}\n')

class Contacto:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.mensajes = []

    def __str__(self):
        return f'{self.nombre} ({self.email})'
    
if __name__ == '__main__':
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()