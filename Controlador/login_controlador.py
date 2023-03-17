from Vista.ventana_login import *


class Login_Controlador:

    def __init__(self, root):
        self.view = Ventana_Login(root)

        self.usuario = self.view.txt_nombre_usuario.get()
        self.password = self.view.txt_password_usuario.get()

        self.view.btnGuardar_texto_escrito.config(command=self.iniciar_sesion(self.usuario, self.password))

    def validacion_datos(self):
   
        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_mineria"
        )
        fcursor=bd.cursor()

        fcursor.execute("SELECT contraseña FROM tlogin WHERE usuario='"+ self.txt_nombre_usuario.get()+"'and contraseña='"+ self.txt_password_usuario.get()+"'")

        if fcursor.fetchall():
            messagebox.showinfo(title="Inicio de sesión correcta", message="Usuario y contraseña correcta")
            self.ventana_uno()
        else: 
            messagebox.showinfo(title="Inicio de sesión incorrecta", message="Usuario y contraseña incorrecta")
            
        bd.close()

    def inserta_datos(self):
        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_mineria"
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

    def iniciar_sesion(self, usuario, password):

        if usuario == "JeSa" and password == "3008":
            self.ventana_uno()
        else:
            print("Datos incorrectos")

    def ventana_uno(self):
        root = tk.Tk()
        Principal_Controlador(root)
        root.mainloop()