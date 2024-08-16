import tkinter as tk
from tkinter import messagebox, ttk
import os


class LoginWindow:
    """
    Ventana de inicio de sesión
    """
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('300x200')
        self.root.minsize(293, 146)  # Establece el tamaño mínimo de la ventana

        # Icono
        ruta_icono = "D:/ProyectosPersonales/Escuela/Formulacion_y_evaluacion_de_proyectos/scr/ico/ICEP_LOGO.png"
        if os.path.exists(ruta_icono):
            icono = tk.PhotoImage(file=ruta_icono)
            self.root.iconphoto(False, icono)
        else:
            messagebox.showerror("Error", "Icono no encontrado")

        # Label y Caja de texto de Usuario
        self.label_username = ttk.Label(root, text="Usuario")
        self.label_username.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.entry_username = ttk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        # Contraseña label y caja de texto
        self.label_password = ttk.Label(root, text="Contraseña")
        self.label_password.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.entry_password = ttk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        # Login boton
        self.button_login = ttk.Button(root, text="Ingresar", command=self.login)
        self.button_login.grid(row=2, columnspan=2, pady=20)

    def login(self):
        """
        Falta agregar la verificación de usuario y contraseña

        Verifica si el usuario y la contraseña son correctos
        :return:

        """
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Verifica si el usuario y la contraseña son correctos
        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login", "Invalid username or password")


if __name__ == '__main__':
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
