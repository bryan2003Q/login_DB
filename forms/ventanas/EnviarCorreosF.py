import tkinter as tk
from tkinter import ttk
import smtplib

class VentanaEnviarCorreo:
    def __init__(self, master):
        self.master = master
        self.master.title("Enviar correo electrónico")
        
        # Crear campos de entrada
        ttk.Label(self.master, text="Destinatario:").grid(column=0, row=0, padx=5, pady=5)
        self.destinatario_entry = ttk.Entry(self.master)
        self.destinatario_entry.grid(column=1, row=0, padx=5, pady=5)
        
        ttk.Label(self.master, text="Asunto:").grid(column=0, row=1, padx=5, pady=5)
        self.asunto_entry = ttk.Entry(self.master)
        self.asunto_entry.grid(column=1, row=1, padx=5, pady=5)
        
        ttk.Label(self.master, text="Mensaje:").grid(column=0, row=2, padx=5, pady=5)
        self.mensaje_text = tk.Text(self.master)
        self.mensaje_text.grid(column=1, row=2, padx=5, pady=5)
        
        # Crear botón de enviar
        enviar_button = ttk.Button(self.master, text="Enviar", command=self.enviar_correo)
        enviar_button.grid(column=1, row=3, padx=5, pady=5)
        
    def enviar_correo(self):
        destinatario = self.destinatario_entry.get()
        asunto = self.asunto_entry.get()
        mensaje = self.mensaje_text.get("1.0", tk.END)
        
        remitente = "tu_correo@gmail.com"
        password = "tu_contraseña"
    
        servidor_smtp = "smtp.gmail.com"
        puerto_smtp = 587
    
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()
        servidor.login(remitente, password)
    
        mensaje_completo = f"Subject: {asunto}\n\n{mensaje}"
    
        servidor.sendmail(remitente, destinatario, mensaje_completo)
    
        servidor.quit()

root = tk.Tk()
app = VentanaEnviarCorreo(root)
root.mainloop()
