

import tkinter as tk
from tkinter import Button, Entry, Label, Listbox, ttk
from tkinter.constants import SUNKEN
import sqlite3

class UI(tk.Frame):
    """Docstring."""    

    
    def __init__(self, parent=None):
       # tk.Frame.__init__(self, parent)
        self.top = tk.Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.parent = parent
        self.centrar_ventana()
        self.init_ui()
        
        self.respuesta=""

    def centrar_ventana(self):
        ancho_ventana=self.top.winfo_reqwidth()
        alto_ventana=self.top.winfo_reqheight()+60
        x_ventana = self.top.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.top.winfo_screenheight() // 2 - alto_ventana // 2
        self.top.resizable(1,1)

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.top.geometry(posicion)


    def init_ui(self):
        """Aqui colocariamos los widgets."""
       # self.title("Selección gráfico")

        conn=sqlite3.connect("grafico.db")
        sql="SELECT NOMBRE FROM grafico ORDER BY NOMBRE"
        cursor=conn.cursor()
        cursor.execute(sql)
        registro=cursor.fetchone()

        self.lista=Listbox(self.top,font=("Arial Bold", 13))
        self.lista.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

        while (registro != None):
                
            self.lista.insert(tk.END,registro[0])
            registro=cursor.fetchone()

        self.btn_aceptar=Button(self.top,text="Aceptar",font=("Arial Bold", 13),command=self.Aceptar)
        self.btn_aceptar.grid(row=2,column=0,padx=5,pady=5)


        self.btn_cancel=Button(self.top,text="Cancelar",font=("Arial Bold", 13))
        self.btn_cancel.grid(row=2,column=1,padx=5,pady=5)

    def Cancelar(self):
        self.respuesta=""

    def Aceptar(self):
        for item in self.lista.curselection():
            self.respuesta=self.lista.get(item)
            print(self.respuesta)
        

if __name__ == "__main__":
    pass
  #  ROOT = tk.Tk()
  #  ROOT.geometry("600x600")
  #  APP=UI(ROOT)
  #  APP.mainloop()