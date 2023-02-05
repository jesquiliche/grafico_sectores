# Importa las librerías necesarias para la aplicación
import decimal
import sqlite3
import dbutil
from sqlite3.dbapi2 import Cursor
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from decimal import *
from tkinter import messagebox
from matplotlib import pyplot
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image
from seleccion_grafico import UI

# Crea la ventana principal
window = Tk()

# Variables para almacenar valores seleccionados
var=IntVar()
var2=IntVar()
var3=IntVar()

entry_var =StringVar()
entry_var2=StringVar()

# Conexión a la base de datos
conn=sqlite3.connect("grafico.db")

# Función para seleccionar un color
def sel_color():
    # Selecciona un color
    micolor=askcolor(color=None)
    # Establece el color en la variable entry_var
    entry_var.set(micolor[1])
    # Configura el fondo del texto txt_Color con el color seleccionado
    txt_Color.configure({"background": micolor[1]})

# Función para establecer el color de texto
def fg_color():
    # Selecciona un color
    micolor=askcolor(color=None)
    # Establece el color en la variable entry_var2
    entry_var2.set(micolor[1])
    # Configura el color de texto de los textos txt_fg y txt_Color con el color seleccionado
    txt_fg.configure({"fg": micolor[1]})
    txt_Color.configure({"fg": micolor[1]})

# Configura el título de la ventana
window.title("Graficos de sectores")

# Dimensiones de la ventana
ancho_ventana = 950
alto_ventana = 540

# Función para centrar la ventana en la pantalla
def centrar_ventana(win):
    # Cálcula la posición x y y de la ventana
    x_ventana = win.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = win.winfo_screenheight() // 2 - alto_ventana // 2
    # Deshabilita la capacidad de redimensionar la ventana
    win.resizable(False,False)
    # Establece la posición y tamaño de la ventana
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    win.geometry(posicion)

# Llama a la función para centrar la ventana
centrar_ventana(window)

# Crea un marco para los datos de las



# Crea el cuadro para los datos introducidos
frame=LabelFrame(window,text="Datos filas",width=ancho_ventana-40,height=250,font=("Arial Bold", 13))
frame.place(x=0,y=0)
frame.grid(row=0,column=0,pady=20,padx=20)

frame2=LabelFrame(window,text="Datos Generales",width=ancho_ventana-40,height=250,font=("Arial Bold", 13))
frame2.place(x=500,y=20,height=485)

frame.grid(row=1,column=0,pady=20,padx=20)


lbl_Etiqueta = Label(frame, text="Etiqueta :",font=("Arial Bold", 13))
lbl_Valor = Label(frame, text="Valor :",font=("Arial Bold", 13))
lbl_Color=Label(frame, text="     ",font=("Arial Bold", 13))
lbl_Titulo=Label(frame2, text="Título :",font=("Arial Bold", 13))


lbl_Etiqueta.grid(row=1,column=0,padx=5,pady=2,sticky="e")
lbl_Valor.grid(row=2,column=0,padx=5,pady=2,sticky="e")
lbl_Color.grid(row=3,column=1,padx=5,pady=2,sticky="e")
lbl_Titulo.grid(row=1,column=2,padx=5,pady=2,sticky="e")

txt_Etiqueta=Entry(frame,width=20,font=("Arial Bold", 13))

validate_entry = lambda text: text.isdecimal()
txt_Valor=Entry(frame,width=20,font=("Arial Bold", 13),
validate="key",validatecommand=(frame.register(validate_entry), "%S"))
txt_Color=Entry(frame,width=10,font=("Arial Bold", 13),
validate="key",validatecommand=(frame.register(validate_entry), ""),
textvariable=entry_var)

 
txt_fg=Entry(frame,width=10,font=("Arial Bold", 13),textvariable=entry_var2,
validate="key",validatecommand=(frame.register(validate_entry), ""))


txt_Titulo=Entry(frame2,width=34,font=("Arial Bold", 13))


lbl_check=Label(frame, text="Extraer:",font=("Arial Bold", 13))
checkbox = ttk.Checkbutton(frame,variable=var,onvalue=1,offvalue=0)

lbl_Leyendas=Label(frame2, text="Leyendas:",font=("Arial Bold", 13))
checkbox2 = ttk.Checkbutton(frame2,variable=var2,onvalue=1,offvalue=0)

lbl_Sombra=Label(frame2, text="Sombra:",font=("Arial Bold", 13))
checkbox3 = ttk.Checkbutton(frame2,variable=var3,onvalue=1,offvalue=0)




txt_Etiqueta.grid(row=1,column=1,padx=20,pady=2,sticky="e")
txt_Valor.grid(row=2,column=1,padx=20,pady=2,sticky="e")
txt_Color.grid(row=3,column=1,padx=20,pady=2,sticky="w")
txt_fg.grid(row=4,column=1,padx=20,pady=2,sticky="w")
lbl_check.grid(row=2,column=2,padx=10,pady=2,sticky="e")

lbl_Leyendas.grid(row=3,column=2,padx=10,pady=2,sticky="e")
lbl_Sombra.grid(row=4,column=2,padx=10,pady=2,sticky="e")

txt_Titulo.grid(row=1,column=3,padx=10,pady=2,sticky="e")
checkbox.grid(row=2,column=3,padx=20,pady=2,sticky="w")

checkbox2.grid(row=3,column=3,padx=10,pady=2,sticky="w")
checkbox3.grid(row=4,column=3,padx=10,pady=2,sticky="w")



def insertar():
    tv.insert("",END,text=txt_Etiqueta.get(),
    values=(txt_Valor.get(),txt_Color.get(),var.get(),entry_var2.get()), tags=('par',))

def borrar():
    
    selected_item = tv.selection()[0] ## get selected item
    if selected_item!="":
        tv.delete(selected_item)
  
btn_Anadir=Button(frame,text="Añadir",font=("Arial Bold", 13),command=insertar)
btn_Anadir.grid(row=5,column=0,padx=20)
btn_Borrar=Button(frame,text="Borrar",font=("Arial Bold", 13),command=borrar)
btn_Borrar.grid(row=5,column=1,padx=20)



btn_Color=Button(frame,text="Bg",font=("Arial Bold", 13),command=sel_color)
btn_Color.grid(row=3,column=0,padx=20,pady=2,columnspan=2,sticky="w")

btn_fg=Button(frame,text="Fg",font=("Arial Bold", 13),command=fg_color)
btn_fg.grid(row=4,column=0,padx=20,pady=2,columnspan=2,sticky="w")




tv =ttk.Treeview(window,columns=("valor","color","explode","fg"),height=13)
tv.delete()
tv.column("#0",width=95)
tv.column("valor",width=95,anchor=CENTER)
tv.column("color",width=90,anchor=CENTER)
tv.column("explode",width=90,anchor=CENTER)
tv.column("fg",width=90,anchor=CENTER)

tv.heading("#0",text="Etiqueta",anchor=CENTER)
tv.heading("valor",text="Valor",anchor=CENTER)
tv.heading("color",text="Color",anchor=CENTER)
tv.heading("explode",text="Explode",anchor=CENTER)
tv.heading("fg",text="fg",anchor=CENTER)

tv.tag_configure('par',background='blue',foreground='black')


style = ttk.Style()
style.configure("Treeview",font=("Arial Bold", 13))
style.configure("Treeview.Heading", font=("Arial Bold", 13))
ScrollVert=Scrollbar(window, command=tv.yview)
ScrollVert.place(y=220,x=480,height=290)

tv.place(y=220,x=20)

def Grafico_tarta():
    

      
    x=tv.get_children()
    etiquetas=[]
    valores=[]
    colores=[]
    explode=[]
    text_color=[]
    y=0
    for item in x:
        datos=dict(tv.item(item))
        etiquetas.append(datos["text"])
        valores.append(datos["values"][0])
        colores.append(datos["values"][1])
        explode.append(int(datos["values"][2])/10)
        text_color.append(datos["values"][3])
       
    if var3.get()==1:

        _, _, texto=pyplot.pie(valores,colors=colores,
        labels=etiquetas,autopct="%1.2f",
        startangle=90,shadow=True,explode=explode)
        print(texto)
    else:
         _, _, texto=pyplot.pie(valores,colors=colores,
        labels=etiquetas,autopct="%1.2f",
        startangle=90,shadow=False,explode=explode)
        
    x=0
    for text in texto:
        text.set_color(text_color[x])
        x=x+1

    
    pyplot.axis("equal")
    if var2.get()==1:
        pyplot.legend(labels=etiquetas)

    pyplot.title(txt_Titulo.get())
    pyplot.show()


btn_Grafico=Button(frame2,text="Gráfico",font=("Arial Bold", 13),command=Grafico_tarta)
btn_Grafico.grid(row=7,column=2,padx=20,pady=2,sticky="w")

#img = PhotoImage(Image.open("GRAFICO.jpg"))
img = PhotoImage(file='GRAFICO.png')



etiqueta=ttk.Label(image=img)
etiqueta.config(image=img)

etiqueta.place(x=510, y=180)

menubar=Menu(window)
window.config(menu=menubar,width=500)






def Guarda_en_base_datos():
    
    d=UI(window)
    window.wait_window(d.top)
    #window.wait_window(APP.top)
    

        # El método grab_set() asegura que no haya eventos 
        # de ratón o teclado que se envíen a otra ventana 
        # diferente a 'self.dialogo'. Se utiliza para 
        # crear una ventana de tipo modal que será 
        # necesario cerrar para poder trabajar con otra
        # diferente. Con ello, también se impide que la 
        # misma ventana se abra varias veces. 
        
   


    sql="SELECT COUNT(*) FROM grafico WHERE NOMBRE='"+txt_Titulo.get()+"'"

    cursor = conn.cursor()
    cursor.execute(sql)
    
    if cursor.fetchone()[0]==0:
        sql=""
        sql=sql+"INSERT INTO grafico(NOMBRE,SOMBRA,LEYENDAS) "
        sql=sql+"VALUES('"+txt_Titulo.get()+"',"+str(var3.get())
        sql=sql+","+str(var2.get())+")"
        conn.execute(sql)
        conn.commit()
        
        sql="SELECT ID FROM grafico WHERE NOMBRE='"+txt_Titulo.get()+"'"
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit
        
        id_grafico = list(cursor.fetchone())[0]
        
        
        x=tv.get_children()
        
        for item in x:
            datos=dict(tv.item(item))
            etiqueta=datos["text"]
            valor=datos["values"][0]
            color=datos["values"][1]
            explode=int(datos["values"][2])
            fg=datos["values"][3]

            sql="INSERT INTO LINEAS_GRAFICO("
            sql=sql+"ID_GRAFICO,ETIQUETA,VALOR,"
            sql=sql+"BG,FG,EXPLODE) VALUES ("
            sql=sql+str(id_grafico)+",'"+etiqueta+"',"
            sql=sql+str(valor)+",'"+color+"','"+fg+"',"
            sql=sql+str(explode)+")"
            print(explode)
            print(sql)
            cursor=conn.cursor()
            print(sql)
            cursor.execute(sql)
            conn.commit()
       
            


    else:
        messagebox.showinfo("Ya existe")

archivoMenu=Menu(menubar,tearoff=0) 
archivoAyuda=Menu(menubar,tearoff=0)

menubar.add_cascade(label="Archivo", menu=archivoMenu)
menubar.add_cascade(label="Ayuda", menu=archivoAyuda)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar",command=Guarda_en_base_datos)
archivoMenu.add_command(label="Borrar")
archivoMenu.add_command(label="Salir")



window.mainloop()
