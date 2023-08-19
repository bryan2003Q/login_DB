import tkinter as tk
from tkinter import messagebox

class Interfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Contactos")
        self.master.geometry("400x400")
        self.master.configure(bg="#f2f2f2")  # Color de fondo
        self.contactos = []

        self.lista_contactos = tk.Listbox(self.master, selectmode=tk.SINGLE, bg="white", font=("Helvetica", 12))
        self.lista_contactos.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.label_nombre = tk.Label(self.master, text='Nombre:', bg="#f2f2f2", font=("Helvetica", 12))
        self.entry_nombre = tk.Entry(self.master, font=("Helvetica", 12))
        self.label_email = tk.Label(self.master, text='Email:', bg="#f2f2f2", font=("Helvetica", 12))
        self.entry_email = tk.Entry(self.master, font=("Helvetica", 12))
        self.boton_nuevo_contacto = tk.Button(self.master, text='Nuevo contacto', command=self.nuevo_contacto, font=("Helvetica", 12))
        
        self.label_nombre.pack()
        self.entry_nombre.pack(fill=tk.BOTH, padx=10)
        self.label_email.pack()
        self.entry_email.pack(fill=tk.BOTH, padx=10)
        self.boton_nuevo_contacto.pack(pady=10)

        self.label_nombre_modificar = tk.Label(self.master, text='Nombre:', bg="#f2f2f2", font=("Helvetica", 12))
        self.entry_nombre_modificar = tk.Entry(self.master, font=("Helvetica", 12))
        self.label_email_modificar = tk.Label(self.master, text='Email:', bg="#f2f2f2", font=("Helvetica", 12))
        self.entry_email_modificar = tk.Entry(self.master, font=("Helvetica", 12))
        self.boton_modificar_contacto = tk.Button(self.master, text='Modificar contacto', command=self.modificar_contacto, font=("Helvetica", 12))

        self.label_nombre_modificar.pack()
        self.entry_nombre_modificar.pack(fill=tk.BOTH, padx=10)
        self.label_email_modificar.pack()
        self.entry_email_modificar.pack(fill=tk.BOTH, padx=10)
        self.boton_modificar_contacto.pack(pady=10)

        self.boton_eliminar_contacto = tk.Button(self.master, text='Eliminar contacto', command=self.eliminar_contacto, font=("Helvetica", 12))
        self.boton_eliminar_contacto.pack(pady=10)

        self.cargar_contactos()

    def nuevo_contacto(self):
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()

        if not nombre or not email:
            messagebox.showinfo("Error", "Por favor, completa los campos de nombre y email.")
            return

        contacto = Contacto(nombre, email)

        self.contactos.append(contacto)
        self.lista_contactos.insert(tk.END, str(contacto))
        self.guardar_contactos()

        self.entry_nombre.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def modificar_contacto(self):
        seleccion = self.lista_contactos.curselection()

        if not seleccion:
            messagebox.showinfo("Error", "Por favor, selecciona un contacto para modificar.")
            return

        indice = seleccion[0]
        contacto = self.contactos[indice]

        nuevo_nombre = self.entry_nombre_modificar.get()
        nuevo_email = self.entry_email_modificar.get()

        if not nuevo_nombre or not nuevo_email:
            messagebox.showinfo("Error", "Por favor, completa los campos de nombre y email.")
            return

        contacto.nombre = nuevo_nombre
        contacto.email = nuevo_email

        self.lista_contactos.delete(indice)
        self.lista_contactos.insert(indice, str(contacto))
        self.guardar_contactos()

        self.entry_nombre_modificar.delete(0, tk.END)
        self.entry_email_modificar.delete(0, tk.END)

    def eliminar_contacto(self):
        seleccion = self.lista_contactos.curselection()

        if not seleccion:
            messagebox.showinfo("Error", "Por favor, selecciona un contacto para eliminar.")
            return

        indice = seleccion[0]

        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este contacto?")

        if confirmar:
            del self.contactos[indice]
            self.lista_contactos.delete(indice)
            self.guardar_contactos()

    def cargar_contactos(self):
        try:
            with open('contactos.txt', 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    partes = linea.strip().split(',')
                    contacto = Contacto(partes[0], partes[1])
                    self.contactos.append(contacto)
                    self.lista_contactos.insert(tk.END, str(contacto))
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