import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql

from Controlador.principal_controlador import *
from Controlador.login_controlador import *

class Ventana_Login:
    def __init__(self):
        self.ventana_login = tk.Tk()
        self.configurar_ventana()
        self.decorar_ventana()
        self.ventana_login.mainloop()

    def configurar_ventana(self):
        self.ventana_login.config(bg="#1D1E22")
        self.ventana_login.title("Inicio de sesión") #Aplica un titulo a la ventana
        self.ventana_login.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 600
        hventana = 400
        wtotal = self.ventana_login.winfo_screenwidth()
        htotal = self.ventana_login.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.ventana_login.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def decorar_ventana(self):
        #Simple label que indica la descripcion del programa
        self.lbl_titulo_descripcion = tk.Label(self.ventana_login, text="Iniciar sesión")
        self.lbl_titulo_descripcion.config(bg="#1D1E22", fg = "#FFBD59", font=('Roboto', '40', 'bold'))
        self.lbl_titulo_descripcion.pack(pady=10)

        self.lbl_nombre_usuario=tk.Label(self.ventana_login,text = "Nombre de usuario" )
        self.lbl_nombre_usuario.config(bg="#1D1E22", fg = "white", font = ('Roboto', '15',))
        self.lbl_nombre_usuario.pack()
        
        self.txt_nombre_usuario = tk.Entry(self.ventana_login, relief="solid")
        self.txt_nombre_usuario.pack(pady=10)

        self.lblPregunta=tk.Label(self.ventana_login,text = "Contraseña" )
        self.lblPregunta.config(bg="#1D1E22", fg = "white", font = ('Roboto', '15',))
        self.lblPregunta.pack(pady=10)
        
        self.txt_password_usuario = tk.Entry(self.ventana_login, relief="solid")
        self.txt_password_usuario.pack(pady=10)

        self.btnGuardar_texto_escrito = tk.Button(self.ventana_login, command = self.iniciar_sesion,text = "Iniciar sesión",width = 10, height = 1)
        self.btnGuardar_texto_escrito.pack(pady=10)

    def menu_ventana_principal(self):
        self.menuppal = tk.Menu(self.ventana_login)
        self.opciones = tk.Menu(self.menuppal)
        self.opciones.add_command(label="Insertar", command = self.ventana_uno)
        self.opciones.add_command(label="Visualizar", command = self.ventana_dos)
        self.opciones.add_command(label="Acerca de", command = self.ventana_tres)
        self.menuppal.add_cascade(label="Opciones", menu=self.opciones)
        self.ventana_login.config(menu=self.menuppal)

    def iniciar_sesion(self):
   
        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_energias"
        )
        fcursor=bd.cursor()

        fcursor.execute("SELECT contraseña FROM tlogin WHERE usuario='"+ self.txt_nombre_usuario.get()+"'and contraseña='"+ self.txt_password_usuario.get()+"'")

        if fcursor.fetchall():
            messagebox.showinfo(title="Inicio de sesión correcta", message="Usuario y contraseña correcta")
            self.ventana_uno()
        else: 
            messagebox.showinfo(title="Inicio de sesión incorrecta", message="Usuario y contraseña incorrecta")
            
        bd.close()

    def registrar_usuario(self):
        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_energias"
        )
        fcursor=bd.cursor()
        
        sql="INSERT INTO tlogin (usuario, contraseña) VALUES('{0}', '{1}')".format(self.txt_nombre_usuario.get(),self.txt_password_usuario.get())

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitoso", title="Aviso")

        except:
            bd.rollback
            messagebox.showinfo(message="Registro anulado", title="Aviso")    

        bd.close()

    def ventana_uno(self):
        root = tk.Tk()
        Principal_Controlador(root)
        root.mainloop()