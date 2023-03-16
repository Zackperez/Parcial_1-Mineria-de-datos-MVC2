import tkinter as tk

class Ventana_Principal(tk.Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.configurar_ventana()
        self.decorar_ventana()
        self.parent.mainloop()

    def configurar_ventana(self):
        self.parent.config(bg="#0D1216")
        self.parent.title("Inicio de sesión") #Aplica un titulo a la ventana
        self.parent.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 610
        hventana = 600
        wtotal = self.parent.winfo_screenwidth()
        htotal = self.parent.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.parent.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def decorar_ventana(self):
        self.btnGuardar_texto_escrito = tk.Button(self.parent,text = "Guardar", command = self.saludar,width = 10, height = 1)
        self.btnGuardar_texto_escrito.grid(row = 1, column = 1,padx = 10, pady = 0)

    def saludar(self):
        print("hola")