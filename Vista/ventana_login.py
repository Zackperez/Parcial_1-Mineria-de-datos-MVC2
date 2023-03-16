import tkinter as tk

from Controlador.login_controlador import *
from Controlador.principal_controlador import *

class Ventana_Login:
    def __init__(self):
        self.ventana_login = tk.Tk()
        self.configurar_ventana()
        self.decorar_ventana()
        self.ventana_login.mainloop()

    def configurar_ventana(self):
        self.ventana_login.config(bg="#0D1216")
        self.ventana_login.title("Inicio de sesión") #Aplica un titulo a la ventana
        self.ventana_login.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 610
        hventana = 600
        wtotal = self.ventana_login.winfo_screenwidth()
        htotal = self.ventana_login.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.ventana_login.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def decorar_ventana(self):

        #Simple label que indica la descripcion del programa
        self.lbl_titulo_descripcion = tk.Label(self.ventana_login, text="Iniciar sesión")
        self.lbl_titulo_descripcion.config(bg="#0D1216", fg = "#FFBD59", font=('Roboto', '25', 'bold'))
        self.lbl_titulo_descripcion.grid(row=0, column=0)

        self.lbl_nombre_usuario=tk.Label(self.ventana_login,text = "Nombre de usuario" )
        self.lbl_nombre_usuario.config(bg="#0D1216", fg = "white", font = ('Roboto', '12',))
        self.lbl_nombre_usuario.grid(row = 2, column = 0, pady=5)
        
        self.txt_nombre_usuario = tk.Entry(self.ventana_login, relief="solid")
        self.txt_nombre_usuario.grid(row = 3, column = 0, ipadx = 20, padx = 10)

        self.lblPregunta=tk.Label(self.ventana_login,text = "Contraseña" )
        self.lblPregunta.config(bg="#0D1216", fg = "white", font = ('Roboto', '12',))
        self.lblPregunta.grid(row = 4, column = 0, pady=5)
        
        self.txt_password_usuario = tk.Entry(self.ventana_login, relief="solid")
        self.txt_password_usuario.grid(row = 5, column = 0, ipadx = 20, padx = 10)

        self.btnGuardar_texto_escrito = tk.Button(self.ventana_login,text = "Guardar", command = self.iniciar_sesion,width = 10, height = 1)
        self.btnGuardar_texto_escrito.grid(row = 6, column = 0,padx = 10, pady = 0)

    def iniciar_sesion(self):
        usuario = self.txt_nombre_usuario.get()
        password = self.txt_password_usuario.get()

        if usuario == "JeSa" and password == "3008":
            self.ventana_uno()
        else:
            print("Datos incorrectos")

    def ventana_uno(self):
        root = tk.Tk()
        Principal_Controlador(root)
        root.mainloop()
