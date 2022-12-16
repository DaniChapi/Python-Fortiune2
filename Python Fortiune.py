import pymysql
import pymysql.cursors
import tkinter
from tkinter import PhotoImage
from tkinter import ttk
from tkinter.messagebox import showinfo

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     password = '',
                     db = 'bddsandwich',
                     charset = 'utf8mb4',
                     cursorclass = pymysql.cursors.DictCursor)


ventana = tkinter.Tk()
ventana.geometry("1300x800")
def LimpiarVentana():
   for widgets in ventana.winfo_children():
      widgets.destroy()

def editprov2(nomb,mail,tel,idi):
    

    with db.cursor () as cursor:
        if nomb is not None:
            sql = 'UPDATE proveedor SET nombre = %s WHERE IDProv = %s'
            val1 = (nomb,idi)
            cursor.execute(sql,val1)
        if mail is not None:
            sql = 'UPDATE proveedor SET email = %s WHERE IDProv = %s'
            val2 = (mail,idi)
            cursor.execute(sql,val2)
        if tel is not None:
            sql = 'UPDATE proveedor SET teléfono = %s WHERE IDProv = %s'
            val3 = (tel,idi)
            cursor.execute(sql,val3)
        
        db.commit()

    showinfo(title="Reply", message = "Proveedor editado correctamente !")

def editprov1(idi):
    LimpiarVentana()

    with db.cursor () as cursor:
        
        try:
            reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Proveedor)
            reboot.grid(column = 6, row = 6)
            sql = ("SELECT nombre, email, teléfono FROM proveedor WHERE IDProv = %s")
            cursor.execute(sql,idi)
            nm = cursor.fetchone()
        
            ti = tkinter.Label(ventana, text = "Antiguo nombre",font=('Times 25'), height=3 , bg = 'cornflower blue')
            ti.grid(column=0, row = 0)

            ti = tkinter.Label(ventana, text = nm['nombre'],font=('Times 15'), height=3 , bg = 'cornflower blue')
            ti.grid(column=1, row = 0)

            ti = tkinter.Label(ventana, text = "Antiguo mail",font=('Times 25'), height=3 , bg = 'cornflower blue')
            ti.grid(column=0, row = 2)
            
            ti = tkinter.Label(ventana, text = nm['email'],font=('Times 15'), height=3 , bg = 'cornflower blue')
            ti.grid(column=1, row = 2)

            ti = tkinter.Label(ventana, text = "Antiguo teléfono",font=('Times 25'), height=3 , bg = 'cornflower blue')
            ti.grid(column=0, row = 4)

            ti = tkinter.Label(ventana, text = nm['teléfono'],font=('Times 15'), height=3 , bg = 'cornflower blue')
            ti.grid(column=1, row = 4)

            eti = tkinter.Label(ventana, text = "Nuevo nombre: ",font=('Times 25'), height=3 , bg = 'cornflower blue')
            eti.grid(column=0, row = 1)
            ing_prov = tkinter.Entry(ventana, font=('Times 25'))
            ing_prov.grid(column=1, row = 1)

            eti2 = tkinter.Label(ventana, text = "Nuevo mail",font=('Times 25'), height=3 , bg = 'cornflower blue')
            eti2.grid(column=0, row = 3)
            ing2_prov = tkinter.Entry(ventana, font=('Times 25'))
            ing2_prov.grid(column=1, row = 3)

            eti3 = tkinter.Label(ventana, text = "Nuevo Teléfono: (+56)",font=('Times 25'), height=3 , bg = 'cornflower blue')
            eti3.grid(column=0, row = 5)
            ing3_prov = tkinter.Entry(ventana, font=('Times 25'))
            ing3_prov.bind("<Return>", (lambda event: editprov2(ing_prov.get(), ing2_prov.get(), ing3_prov.get(), idi)))
            ing3_prov.grid(column=1, row = 5)
        

           
        except Exception as e:
            raise
        


def entertext(nomb,mail,tel,desc):
    showinfo(title="Reply", message = "%s agregado a la lista!" % nomb)
    with db.cursor () as cursor:
        sql = "INSERT INTO proveedor (nombre, email, teléfono,descripcion) VALUES (%s,%s,%s,%s)"
        val = (nomb,mail,tel,desc)
        cursor.execute(sql,val)
        db.commit()
    
def eliminar(ID):
    
    with db.cursor () as cursor:
 
        sql = "DELETE FROM proveedor WHERE IDProv = %s"
        cursor.execute(sql,ID)
        db.commit()
        showinfo(title="Reply", message = "Eliminado %s!" % ID)


def PROV1():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Nombre proveedor: ",font=('Times 25'), height=3 , bg = 'cornflower blue')
    eti.pack()
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.pack()

    eti2 = tkinter.Label(ventana, text = "Email: ",font=('Times 25'), height=3 , bg = 'cornflower blue')
    eti2.pack()
    ing2_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing2_prov.pack()

    eti3 = tkinter.Label(ventana, text = "Teléfono: (+56)",font=('Times 25'), height=3 , bg = 'cornflower blue')
    eti3.pack()
    ing3_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing3_prov.pack()

    eti4 = tkinter.Label(ventana, text = "Descripción: ",font=('Times 25'), height=3 , bg = 'cornflower blue')
    eti4.pack()
    ing4_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing4_prov.bind("<Return>", (lambda event: entertext(ing_prov.get(), ing2_prov.get(), ing3_prov.get(),ing4_prov.get())))
    ing4_prov.pack()


    aux = tkinter.Label(ventana, text = "LISTA PROVEEDORES: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.pack(side = tkinter.LEFT)
 
    with db.cursor () as cursor:
        sql = "SELECT nombre, IDProv IDProv FROM proveedor"
        cursor.execute(sql)
        nombres = cursor.fetchall ()

    for result in nombres:
                
                listaprov = tkinter.Label(ventana, text = result['IDProv'],font=('Times 14 underline bold'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)


                listaprov = tkinter.Label(ventana, text = "       -       ",font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)
              

    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Proveedor)
    reboot.pack()
    reboot.place(x = 0, y = 0)

def PROV2():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingrese ID de proveedor a editar:  ",font=('Times 25'), height=3, bg = 'cornflower blue')
    eti.pack()
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.bind("<Return>", (lambda event: editprov1(ing_prov.get())))
    ing_prov.pack()

    aux = tkinter.Label(ventana, text = "LISTA PROVEEDORES: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.pack(side = tkinter.LEFT)

    with db.cursor () as cursor:
        sql = "SELECT nombre, IDProv IDProv FROM proveedor"
        cursor.execute(sql)
        nombres = cursor.fetchall ()

    for result in nombres:
                
                listaprov = tkinter.Label(ventana, text = result['IDProv'],font=('Times 14 underline bold'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)


                listaprov = tkinter.Label(ventana, text = "       -       ",font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)

    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Proveedor)
    reboot.pack()
    reboot.place(x = 0, y = 0)

def PROV3():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingrese ID de proveedor a ELIMINAR: " ,font=('Times 25'), height=3, bg = 'cornflower blue')
    eti.pack()
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.bind("<Return>", (lambda event: eliminar(ing_prov.get())))
    ing_prov.pack()

    aux = tkinter.Label(ventana, text = "LISTA PROVEEDORES: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.pack(side = tkinter.LEFT)

    with db.cursor () as cursor:
        sql = "SELECT nombre, IDProv IDProv FROM proveedor"
        cursor.execute(sql)
        nombres = cursor.fetchall ()

    for result in nombres:
                
                listaprov = tkinter.Label(ventana, text = result['IDProv'],font=('Times 14 underline bold'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)


                listaprov = tkinter.Label(ventana, text = "       -       ",font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.pack(side = tkinter.LEFT)

    
    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Proveedor)
    reboot.pack(ipadx=40, ipady=20)
    reboot.place(x = 0, y = 0)
    
def PROV4():
    LimpiarVentana()
    with db.cursor () as cursor:
        sql = "SELECT IDProv FROM proveedor"
        cursor.execute(sql)
        IDs = cursor.fetchall ()

    eti = tkinter.Label(ventana, text = "ID Prov",font=('Times 15 underline bold'), height=3, width=10, bg = 'cornflower blue')
    eti.grid(column = 0, row = 0)

    eti = tkinter.Label(ventana, text = "  -  ",font=('Times 15'), height=3, bg = 'cornflower blue')
    eti.grid(column = 1, row = 0)

    eti = tkinter.Label(ventana, text = "Nombre",font=('Times 15 underline bold'), height=3, width=10, bg = 'cornflower blue')
    eti.grid(column = 2, row = 0)

    eti = tkinter.Label(ventana, text = "  -  ",font=('Times 15'), height=3, bg = 'cornflower blue')
    eti.grid(column = 3, row = 0)

    eti = tkinter.Label(ventana, text = "Telefono",font=('Times 15 underline bold'), height=3, width=10, bg = 'cornflower blue')
    eti.grid(column = 4, row = 0)

    eti = tkinter.Label(ventana, text = "  -  ",font=('Times 15'), height=3, bg = 'cornflower blue')
    eti.grid(column = 5, row = 0)

    eti = tkinter.Label(ventana, text = "Mail.",font=('Times 15 underline bold'), height=3, width=10, bg = 'cornflower blue')
    eti.grid(column = 6, row = 0)

    eti = tkinter.Label(ventana, text = "  -  ",font=('Times 15'), height=3, bg = 'cornflower blue')
    eti.grid(column = 7, row = 0)

    eti = tkinter.Label(ventana, text = "Descripción.",font=('Times 15 underline bold'), height=3, width=10, bg = 'cornflower blue')
    eti.grid(column = 8, row = 0)
   
    
    i = 1
    for ID in IDs:
        i = i + 1
        eti = tkinter.Label(ventana, text = ID['IDProv'],font=('Times 13'), height=5, width=10, bg = 'cornflower blue')
        eti.grid(column = 0, row = i)


    with db.cursor () as cursor:
        sql = "SELECT nombre FROM proveedor"
        cursor.execute(sql)
        nombres = cursor.fetchall ()
    
    i = 1
    for nombre in nombres:
        i = i + 1
        eti2 = tkinter.Label(ventana, text = nombre['nombre'],font=('Times 13'), height=5, width=10, bg = 'cornflower blue')
        eti2.grid(column = 2, row = i)


    with db.cursor () as cursor:
        sql = "SELECT teléfono FROM proveedor"
        cursor.execute(sql)
        tfs = cursor.fetchall ()
    
    i = 1
    for tf in tfs:
        i = i + 1
        eti3 = tkinter.Label(ventana, text = tf['teléfono'],font=('Times 13'), height=5, width=10, bg = 'cornflower blue')
        eti3.grid(column = 4, row = i)

    with db.cursor () as cursor:
        sql = "SELECT email FROM proveedor"
        cursor.execute(sql)
        mails = cursor.fetchall ()
    
    i = 1
    for mail in mails:
        i = i + 1
        eti3 = tkinter.Label(ventana, text = mail['email'],font=('Times 13'), height=5, bg = 'cornflower blue')
        eti3.grid(column = 6, row = i)

    with db.cursor () as cursor:
        sql = "SELECT descripcion FROM proveedor"
        cursor.execute(sql)
        descs = cursor.fetchall ()
    
    i = 1
    for desc in descs:
        i = i + 1
        eti3 = tkinter.Label(ventana, text = desc['descripcion'],font=('Times 13'), height=5, bg = 'cornflower blue')
        eti3.grid(column = 8, row = i)

    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Proveedor)
    reboot.grid(column = 9, row = i+1)

def nombreCOMIDA(n1,n2):
    showinfo(title="Reply", message = "%s agregado a la lista!" % n1)
    with db.cursor () as cursor:
        sql = "INSERT INTO producto (nombre, categoría) VALUES (%s,%s)"
        val = (n1,n2)
        cursor.execute(sql,val)
        db.commit()


def IngCOMIDA(n1,n2,n):
    showinfo(title="Reply", message = "%s agregado a la lista!" % n1)
    with db.cursor () as cursor:
        sql = "INSERT INTO producto (nombre, idc, ingredientes) VALUES (%s,%s,%s) "
        val = (n1,n2,n)
        cursor.execute(sql,val)
        db.commit()
        


def COMIDA():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "AÑADIR PRODUCTO ",font=('Chiller 40 underline'),height = 1, bg = 'cornflower blue')
    eti.grid(column=1,row=0)

    eti = tkinter.Label(ventana, text = "Ingresa nombre del producto: ",font=('Times 15'), height=5 , bg = 'cornflower blue')
    eti.grid(column=0,row=1)
    ing_prov = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov.grid(column=1,row=1)

    eti = tkinter.Label(ventana, text = "Ingresa ID de categoría correspondiente: ",font=('Times 15'), height=5 , bg = 'cornflower blue')
    eti.grid(column=0,row=2)
    ing_prov2 = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov2.grid(column=1,row=2)

    eti = tkinter.Label(ventana, text = "Ingresa receta: ",font=('Times 12'), height=5 , bg = 'cornflower blue',textvariable=int)
    eti.grid(column=0,row=3)
    ing_prov3 = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov3.bind("<Return>", (lambda event: IngCOMIDA(ing_prov.get(),ing_prov2.get(), ing_prov3.get())))
    ing_prov3.grid(column=1,row=3)

    aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
    aux.grid(column=2,row=4)

    aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=3,row=4)
    with db.cursor () as cursor:
        sql2 = "SELECT idc, nombre FROM categoria"
        cursor.execute(sql2)
        nombres = cursor.fetchall ()
    i=5
    for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=2,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=3,row=i)
                

              

    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid(column=4,row=i+1)

def editpd2(nomb,cat,idi):
    

    with db.cursor () as cursor:
        if nomb is not None:
            sql = 'UPDATE producto SET nombre = %s WHERE IDPd = %s'
            val1 = (nomb,idi)
            cursor.execute(sql,val1)
        if cat is not None:
            sql = 'UPDATE producto SET idc = %s WHERE IDPd = %s'
            val2 = (cat,idi)
            cursor.execute(sql,val2)
        
        db.commit()

    showinfo(title="Reply", message = "Producto editado correctamente !")

def editpd(idi):
    LimpiarVentana()

    with db.cursor () as cursor:
        
        try:
            reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
            reboot.grid(column = 15, row = 15)
            sql = ("SELECT nombre, idc FROM producto WHERE IDPd = %s")
            cursor.execute(sql,idi)
            nm = cursor.fetchone()
        
            ti = tkinter.Label(ventana, text = "Antiguo nombre: ",font=('Times 25'), height=2 , bg = 'cornflower blue')
            ti.grid(column=0, row = 0)

            ti = tkinter.Label(ventana, text = nm['nombre'],font=('Times 15'), height=2 , bg = 'cornflower blue')
            ti.grid(column=1, row = 0)

            ti = tkinter.Label(ventana, text = "Antigua ID de categoría: ",font=('Times 25'), height=2 , bg = 'cornflower blue')
            ti.grid(column=0, row = 2)
            
            ti = tkinter.Label(ventana, text = nm['idc'],font=('Times 15'), height=2 , bg = 'cornflower blue')
            ti.grid(column=1, row = 2)


            eti = tkinter.Label(ventana, text = "Nuevo nombre: ",font=('Times 25'), height=2 , bg = 'cornflower blue')
            eti.grid(column=0, row = 1)
            ing_prov = tkinter.Entry(ventana, font=('Times 25'))
            ing_prov.grid(column=1, row = 1)

            eti2 = tkinter.Label(ventana, text = "Nueva categoría",font=('Times 25'), height=2 , bg = 'cornflower blue')
            eti2.grid(column=0, row = 3)
            ing2_prov = tkinter.Entry(ventana, font=('Times 25'))
            ing2_prov.bind("<Return>", (lambda event: editpd2(ing_prov.get(), ing2_prov.get(), idi)))
            ing2_prov.grid(column=1, row = 3)

            aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
            aux.grid(column=0,row=4)

            aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
            aux.grid(column=1,row=4)
            with db.cursor () as cursor:
                sql2 = "SELECT idc, nombre FROM categoria"
                cursor.execute(sql2)
                nombres = cursor.fetchall ()
            i=5
            for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)

        except Exception as e:
            raise
    
def COMIDA22(idcat):
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingrese ID de producto para editar:  ",font=('Times 15'), height=3, bg = 'cornflower blue')
    eti.grid(column=0,row=0)
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.bind("<Return>", (lambda event: editpd(ing_prov.get())))
    ing_prov.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "IDs: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=0,row=1)

    aux = tkinter.Label(ventana, text = "LISTA PRODUCTOS: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=1)

    with db.cursor () as cursor:
        sql = "SELECT nombre, IDPd FROM producto WHERE idc = %s"
        cursor.execute(sql,idcat)
        nombres = cursor.fetchall ()
    i = 2
    for result in nombres:
                
                listaprov = tkinter.Label(ventana, text = result['IDPd'],font=('Times 14 underline bold'), bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'),  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)
                i=i+1


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid()

def COMIDA2():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingresa ID de categoría: ",font=('Times 12'), height=5 , bg = 'cornflower blue',textvariable=int)
    eti.grid(column=0,row=0)
    ing_prov3 = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov3.bind("<Return>", (lambda event: COMIDA22(ing_prov3.get())))
    ing_prov3.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
    aux.grid(column=0,row=1)

    aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=1)
    with db.cursor () as cursor:
        sql2 = "SELECT idc, nombre FROM categoria"
        cursor.execute(sql2)
        nombres = cursor.fetchall ()
    i=2
    for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid(column=4,row=i+1)

def eliminar2(ID):
    with db.cursor () as cursor:
 
        sql = "DELETE FROM producto WHERE IDPd = %s"
        cursor.execute(sql,ID)
        db.commit()
        showinfo(title="Reply", message = "Eliminado %s!" % ID)

def COMIDA32(idcat):
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingrese ID de producto a ELIMINAR " ,font=('Times 25'), height=3, bg = 'cornflower blue')
    eti.grid(column=0,row=0)
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.bind("<Return>", (lambda event: eliminar2(ing_prov.get())))
    ing_prov.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "IDs: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=0,row=1)

    aux = tkinter.Label(ventana, text = "LISTA PRODUCTOS: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=1)

    with db.cursor () as cursor:
        sql = "SELECT nombre, IDPd FROM producto WHERE idc = %s"
        cursor.execute(sql,idcat)
        nombres = cursor.fetchall ()
    i = 2
    for result in nombres:
                
                listaprov = tkinter.Label(ventana, text = result['IDPd'],font=('Times 14 underline bold'), bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'),  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)
                i=i+1


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid()

def COMIDA3():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingresa ID de categoría: ",font=('Times 12'), height=5 , bg = 'cornflower blue',textvariable=int)
    eti.grid(column=0,row=0)
    ing_prov3 = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov3.bind("<Return>", (lambda event: COMIDA32(ing_prov3.get())))
    ing_prov3.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
    aux.grid(column=0,row=1)

    aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=1)
    with db.cursor () as cursor:
        sql2 = "SELECT idc, nombre FROM categoria"
        cursor.execute(sql2)
        nombres = cursor.fetchall ()
    i=2
    for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid(column=4,row=i+1)

def VerComidas(IDcat):
    LimpiarVentana()
    listaprov = tkinter.Label(ventana, text = "ID",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=0,row=0)

    listaprov = tkinter.Label(ventana, text = "-",font=('Times 14 '), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=1,row=0)

    listaprov = tkinter.Label(ventana, text = "NOMBRE",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=2,row=0)

    listaprov = tkinter.Label(ventana, text = "-",font=('Times 14'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=3,row=0)

    listaprov = tkinter.Label(ventana, text = "RECETA",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=4,row=0)

    with db.cursor () as cursor:
        sql = "SELECT nombre, IDPd, ingredientes FROM producto WHERE idc = %s"
        cursor.execute(sql, IDcat)
        nombres = cursor.fetchall ()
    
    i = 0
    for result in nombres:
                i=i+1

                listaprov = tkinter.Label(ventana, text = result['IDPd'],font=('Times 14'), bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), bg = 'cornflower blue')
                listaprov.grid(column=2,row=i)

                listaprov = tkinter.Label(ventana, text = result['ingredientes'],font=('Times 14'), bg = 'cornflower blue')
                listaprov.grid(column=4,row=i)


    reboot = tkinter.Button(ventana, text = "Volver atrás.", bg = "Gray", command = COMIDA4)
    reboot.grid(column = 0, row = i+1)

def COMIDA4():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingresa ID de categoría: ",font=('Times 12'), height=5 , bg = 'cornflower blue',textvariable=int)
    eti.grid(column=0,row=0)
    ing_prov3 = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov3.bind("<Return>", (lambda event: VerComidas(ing_prov3.get())))
    ing_prov3.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
    aux.grid(column=0,row=1)

    aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=1)
    with db.cursor () as cursor:
        sql2 = "SELECT idc, nombre FROM categoria"
        cursor.execute(sql2)
        nombres = cursor.fetchall ()
    i=2
    for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid(column=4,row=i+1)

def editrec(ing,idi):
    

    with db.cursor () as cursor:
        if ing is not None:
            sql = 'UPDATE producto SET ingredientes = %s WHERE IDPd = %s'
            val1 = (ing,idi)
            cursor.execute(sql,val1)
        
        db.commit()

    showinfo(title="Reply", message = "Receta editada correctamente !")

def EditarReceta(idi):
    LimpiarVentana()

    with db.cursor () as cursor:
        
        try:
            reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
            reboot.grid(column = 6, row = 6)
            sql = ("SELECT nombre, ingredientes FROM producto WHERE IDPd = %s")
            cursor.execute(sql,idi)
            nm = cursor.fetchone()

            ti = tkinter.Label(ventana, text = "Antigua receta: ",font=('Times 25'), height=3 , bg = 'cornflower blue')
            ti.grid(column=0, row = 2)
            
            ti = tkinter.Label(ventana, text = nm['ingredientes'],font=('Times 15'), height=3 , bg = 'cornflower blue')
            ti.grid(column=1, row = 2)


            eti = tkinter.Label(ventana, text = "Nueva receta: ",font=('Times 25'), height=3 , bg = 'cornflower blue')
            eti.grid(column=0, row = 1)
            ing_prov = tkinter.Entry(ventana, font=('Times 25'))
            ing_prov.bind("<Return>", (lambda event: editrec(ing_prov.get(), idi)))
            ing_prov.grid(column=1, row = 1)
            
        except Exception as e:
            raise

def COMIDA52(IDCat):
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingrese ID de producto para editar receta:  ",font=('Times 15'), height=3, bg = 'cornflower blue')
    eti.grid(column=0,row=0)
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.bind("<Return>", (lambda event: EditarReceta(ing_prov.get())))
    ing_prov.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "IDs: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=0,row=1)

    aux = tkinter.Label(ventana, text = "LISTA PRODUCTOS: ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=1)

    with db.cursor () as cursor:
        sql = "SELECT nombre, IDPd FROM producto WHERE idc = %s"
        cursor.execute(sql,IDCat)
        nombres = cursor.fetchall ()
    i = 2
    for result in nombres:
                
                listaprov = tkinter.Label(ventana, text = result['IDPd'],font=('Times 14 underline bold'), bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'),  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)
                i=i+1


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid()

def COMIDA5():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingresa ID de categoría: ",font=('Times 20'), height=2 , bg = 'cornflower blue',textvariable=int)
    eti.grid(column=0,row=0)
    ing_prov3 = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov3.bind("<Return>", (lambda event: COMIDA52(ing_prov3.get())))
    ing_prov3.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
    aux.grid(column=0,row=2)

    aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=2)
    with db.cursor () as cursor:
        sql2 = "SELECT idc, nombre FROM categoria"
        cursor.execute(sql2)
        nombres = cursor.fetchall ()
    i=3
    for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)
                


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid(column=4,row=i+1)


def Añainsumo(n1,n2):
    i = 0
    showinfo(title="Reply", message = "%s agregado a la lista!" % n1)
    with db.cursor () as cursor:
        sql = "INSERT INTO insumo (nombre, stock) VALUES (%s,%s)"
        val = (n1,n2)
        cursor.execute(sql,val)
        db.commit()
        


def Añadir():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "AÑADIR INSUMO ",font=('Chiller 40 underline'),height = 1, bg = 'cornflower blue')
    eti.grid(column=1,row=0)

    eti = tkinter.Label(ventana, text = "Ingresa nombre del insumo: ",font=('Times 15'), height=5 , bg = 'cornflower blue')
    eti.grid(column=0,row=1)
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.grid(column=1,row=1)

    eti = tkinter.Label(ventana, text = "Ingresa Stock: ",font=('Times 15'), height=5 , bg = 'cornflower blue')
    eti.grid(column=0,row=2)
    ing_prov3 = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov3.bind("<Return>", (lambda event: Añainsumo(ing_prov.get(), ing_prov3.get())))
    ing_prov3.grid(column=1,row=2)

              
    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Inventario)
    reboot.grid(column=4,row=4)

def eliminar3(ID):
    with db.cursor () as cursor:
 
        sql = "DELETE FROM insumo WHERE IDi = %s"
        cursor.execute(sql,ID)
        db.commit()
        showinfo(title="Reply", message = "%s eliminado!" % ID)

def Borrar():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingrese ID de insumo a ELIMINAR" ,font=('Times 25'), height=3, bg = 'cornflower blue')
    eti.grid(column=0,row=0)
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.bind("<Return>", (lambda event: eliminar3(ing_prov.get())))
    ing_prov.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "ID",font=('Times 15 underline bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=2,row=0)

    aux = tkinter.Label(ventana, text = "INVENTARIO ",font=('Times 15 underline bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=3,row=0)

    with db.cursor () as cursor:
        sql = "SELECT nombre, IDi FROM insumo"
        cursor.execute(sql)
        nombres = cursor.fetchall ()
    i = 0
    j = 0
    for result in nombres:
            i = i + 1
            if i <= 23:
                listaprov = tkinter.Label(ventana, text = result['IDi'],font=('Times 14  bold'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=2,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=3,row=i)
            if i > 23:
                j = j + 1
                listaprov = tkinter.Label(ventana, text = result['IDi'],font=('Times 14  bold'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=4,row=j)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=5,row=j)


    
    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Inventario)
    reboot.grid(column=6,row=0)

def e2(ID):
    with db.cursor () as cursor:
        sql = "UPDATE insumo SET stock = stock + %s WHERE IDi = %s"
        val = (1,ID)
        cursor.execute(sql,val)
        db.commit()
    edin(ID)

def e3(ID):
    with db.cursor () as cursor:
        sql = "UPDATE insumo SET stock = stock + %s WHERE IDi = %s"
        val = (10,ID)
        cursor.execute(sql,val)
        db.commit()
    edin(ID)

def e4(ID):
    with db.cursor () as cursor:
        sql = "UPDATE insumo SET stock = stock - %s WHERE IDi = %s"
        val = (1,ID)
        cursor.execute(sql,val)
        db.commit()
    edin(ID)

def e5(ID):
    with db.cursor () as cursor:
        sql = "UPDATE insumo SET stock = stock - %s WHERE IDi = %s"
        val = (10,ID)
        cursor.execute(sql,val)
        db.commit()
    edin(ID)


def edin(ID):
    with db.cursor () as cursor:
        sql = "SELECT stock FROM insumo WHERE IDi = %s"
        cursor.execute(sql,ID)
        ida = cursor.fetchone()

    LimpiarVentana()
    pbot1 = tkinter.Button(ventana, text = "+1 STOCK", bg = "Light green", activebackground = "green", command = lambda: e2(ID))
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)

    pbot1 = tkinter.Button(ventana, text = "+10 STOCK", bg = "Light green", activebackground = "green", command = lambda: e3(ID))
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)

    pbot1 = tkinter.Button(ventana, text = "-1 STOCK", bg = "Light green", activebackground = "green", command = lambda: e4(ID))
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)

    pbot1 = tkinter.Button(ventana, text = "-10 STOCK", bg = "Light green", activebackground = "green", command = lambda: e5(ID))
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)

    eti = tkinter.Label(ventana, text = "STOCK: " ,font=('Times 25'), height=3, bg = 'cornflower blue')
    eti.pack()

    eti2 = tkinter.Label(ventana, text = ida["stock"] ,font=('Times 25'), height=3, bg = 'cornflower blue')
    eti2.pack()

    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Inventario)
    reboot.pack()
    reboot.place(x = 0, y = 0)


def Editar():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingrese ID de insumo a editar" ,font=('Times 25'), height=3, bg = 'cornflower blue')
    eti.grid(column=0,row=0)
    ing_prov = tkinter.Entry(ventana, font=('Times 25'))
    ing_prov.bind("<Return>", (lambda event: edin(ing_prov.get())))
    ing_prov.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "ID",font=('Times 15 underline bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=2,row=0)

    aux = tkinter.Label(ventana, text = "INVENTARIO ",font=('Times 15 underline bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=3,row=0)

    with db.cursor () as cursor:
        sql = "SELECT nombre, IDi FROM insumo"
        cursor.execute(sql)
        nombres = cursor.fetchall ()
    i = 0
    j = 0
    for result in nombres:
            i = i + 1
            if i <= 23:
                listaprov = tkinter.Label(ventana, text = result['IDi'],font=('Times 14  bold'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=2,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=3,row=i)
            if i > 23:
                j = j + 1
                listaprov = tkinter.Label(ventana, text = result['IDi'],font=('Times 14  bold'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=4,row=j)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14 bold'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=5,row=j)


    
    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Inventario)
    reboot.grid(column=6,row=0)


def Mostrar():
    LimpiarVentana()
    listaprov = tkinter.Label(ventana, text = "ID",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=0,row=0)

    listaprov = tkinter.Label(ventana, text = "-",font=('Times 14 '), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=1,row=0)

    listaprov = tkinter.Label(ventana, text = "NOMBRE",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=2,row=0)

    listaprov = tkinter.Label(ventana, text = "-",font=('Times 14'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=3,row=0)

    listaprov = tkinter.Label(ventana, text = "STOCK",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=4,row=0)

    listaprov = tkinter.Label(ventana, text = "-",font=('Times 14'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=5,row=0)

    listaprov = tkinter.Label(ventana, text = "ID",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=6,row=0)

    listaprov = tkinter.Label(ventana, text = "-",font=('Times 14 '), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=7,row=0)

    listaprov = tkinter.Label(ventana, text = "NOMBRE",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=8,row=0)

    listaprov = tkinter.Label(ventana, text = "-",font=('Times 14'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=9,row=0)

    listaprov = tkinter.Label(ventana, text = "STOCK",font=('Times 14 underline bold'), height = 3,  bg = 'cornflower blue')
    listaprov.grid(column=10,row=0)

    with db.cursor () as cursor:
        sql = "SELECT IDi, nombre, Stock FROM insumo"
        cursor.execute(sql)
        nombres = cursor.fetchall ()
    
    i = 0
    j = 0
    for result in nombres:
                i=i+1
                
                if i <= 23:
                    listaprov = tkinter.Label(ventana, text = result['IDi'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                    listaprov.grid(column=0,row=i)

                    listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                    listaprov.grid(column=2,row=i)

                    listaprov = tkinter.Label(ventana, text = result['Stock'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                    listaprov.grid(column=4,row=i)
                if i > 23:
                    j=j+1
                    listaprov = tkinter.Label(ventana, text = result['IDi'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                    listaprov.grid(column=6,row=j)

                    listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                    listaprov.grid(column=8,row=j)

                    listaprov = tkinter.Label(ventana, text = result['Stock'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                    listaprov.grid(column=10,row=j)


    reboot = tkinter.Button(ventana, text = "Volver atrás.", bg = "Gray", command = Inventario)
    reboot.grid(column = 11, row = i+1)

def Aña(cat):
    showinfo(title="Reply", message = "%s agregada!" % cat)
    with db.cursor () as cursor:
        sql = "INSERT INTO categoria (nombre) VALUES (%s)"
        cursor.execute(sql,cat)
        db.commit()

def Añcat():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingresa nueva categoría: ",font=('Times 12'), height=5 , bg = 'cornflower blue',textvariable=int)
    eti.grid(column=0,row=0)
    ing_prov3 = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov3.bind("<Return>", (lambda event: Aña(ing_prov3.get())))
    ing_prov3.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
    aux.grid(column=0,row=1)

    aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=1)
    with db.cursor () as cursor:
        sql2 = "SELECT idc, nombre FROM categoria"
        cursor.execute(sql2)
        nombres = cursor.fetchall ()
    i=2
    for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid(column=4,row=i+1)
              

def ec3(nm,idcat):
    with db.cursor () as cursor:
        sql = 'UPDATE categoria SET nombre = %s WHERE idc = %s'
        val = (nm,idcat)
        cursor.execute(sql,val)
        db.commit()

    showinfo(title="Reply", message = "Categoría editada correctamente !")

def ec2(idcat):
    LimpiarVentana()

    with db.cursor () as cursor:
        
        try:
            reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
            reboot.grid(column = 15, row = 15)
            sql = ("SELECT nombre FROM categoria WHERE idc = %s")
            cursor.execute(sql,idcat)
            nm = cursor.fetchone()
        
            ti = tkinter.Label(ventana, text = "Antigua categoría: ",font=('Times 25'), height=2 , bg = 'cornflower blue')
            ti.grid(column=0, row = 0)

            ti = tkinter.Label(ventana, text = nm['nombre'],font=('Times 15'), height=2 , bg = 'cornflower blue')
            ti.grid(column=1, row = 0)


            eti2 = tkinter.Label(ventana, text = "Nuevo nombre: ",font=('Times 25'), height=2 , bg = 'cornflower blue')
            eti2.grid(column=0, row = 2)
            ing2_prov = tkinter.Entry(ventana, font=('Times 25'))
            ing2_prov.bind("<Return>", (lambda event: ec3(ing2_prov.get(),idcat)))
            ing2_prov.grid(column=1, row = 2)

            aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
            aux.grid(column=0,row=3)

            aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
            aux.grid(column=1,row=3)
            with db.cursor () as cursor:
                sql2 = "SELECT idc, nombre FROM categoria"
                cursor.execute(sql2)
                nombres = cursor.fetchall ()
            i=4
            for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)

        except Exception as e:
            raise
def editcat():
    LimpiarVentana()
    eti = tkinter.Label(ventana, text = "Ingresa ID de categoría: ",font=('Times 12'), height=5 , bg = 'cornflower blue',textvariable=int)
    eti.grid(column=0,row=0)
    ing_prov3 = tkinter.Entry(ventana, font=('Times 20'))
    ing_prov3.bind("<Return>", (lambda event: ec2(ing_prov3.get())))
    ing_prov3.grid(column=1,row=0)

    aux = tkinter.Label(ventana, text = "ID ",font=('Times 15 bold'),width = 5, bg = 'cornflower blue')
    aux.grid(column=0,row=1)

    aux = tkinter.Label(ventana, text = "CATEGORÍAS ",font=('Times 15 bold'), height=3, bg = 'cornflower blue')
    aux.grid(column=1,row=1)
    with db.cursor () as cursor:
        sql2 = "SELECT idc, nombre FROM categoria"
        cursor.execute(sql2)
        nombres = cursor.fetchall ()
    i=2
    for result in nombres:
                i=i+1
                listaprov = tkinter.Label(ventana, text = result['idc'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=0,row=i)

                listaprov = tkinter.Label(ventana, text = result['nombre'],font=('Times 14'), height = 1,  bg = 'cornflower blue')
                listaprov.grid(column=1,row=i)


    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = Producto)
    reboot.grid(column=4,row=i+1)


def Categorias():
    LimpiarVentana()
    prov = tkinter.Label(ventana, text = "CATEGORÍAS.",font=('Chiller 40 underline bold'), height=3, bg = 'cornflower blue')
    prov.pack()
    pbot1 = tkinter.Button(ventana, text = "Añadir categoría.", bg = "Light green", activebackground = "green", command = Añcat)
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)

    pbot1 = tkinter.Button(ventana, text = "Editar categoría.", bg = "Light green", activebackground = "green", command = editcat)
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20) 
    
    reboot = tkinter.Button(ventana, text = "Volver atrás.", bg = "Gray", command = Producto)
    reboot.pack(padx = 10, pady = 10,ipadx=40, ipady=20)

def Proveedor():
    LimpiarVentana()
    prov = tkinter.Label(ventana, text = "PROVEEDOR.",font=('Chiller 40 underline bold'), height=3, bg = 'cornflower blue')
    prov.pack()
    pbot1 = tkinter.Button(ventana, text = "Ingresar nuevo proveedor.", bg = "Light green", activebackground = "green", command = PROV1)
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot2 = tkinter.Button(ventana, text = "Editar/actualizar proveedor.", bg = "Light green", activebackground = "green", command = PROV2)
    pbot2.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot3 = tkinter.Button(ventana, text = "Eliminar proveedor.", bg = "Light green", activebackground = "green", command = PROV3)
    pbot3.pack(padx = 10, pady = 10,ipadx=40, ipady=20)
    pbot4 = tkinter.Button(ventana, text = "Mostrar proveedores.", bg = "Light green", activebackground = "green", command = PROV4)
    pbot4.pack(padx = 10, pady = 10,ipadx=40, ipady=20)
    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = menu)
    reboot.pack(padx = 10, pady = 10,ipadx=40, ipady=20)

def Inventario(): 
    LimpiarVentana()
    prov = tkinter.Label(ventana, text = "INVENTARIO.",font=('Chiller 40 underline bold'), height=3, bg = 'cornflower blue')
    prov.pack()
    pbot1 = tkinter.Button(ventana, text = "Añadir insumo.", bg = "Light green", activebackground = "green", command = Añadir)
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot1 = tkinter.Button(ventana, text = "Eliminar insumo.", bg = "Light green", activebackground = "green", command = Borrar)
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot1 = tkinter.Button(ventana, text = "Actualizar stock", bg = "Light green", activebackground = "green", command = Editar)
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)     
    pbot2 = tkinter.Button(ventana, text = "Mostrar stock de insumos.", bg = "Light green", activebackground = "green", command = Mostrar)
    pbot2.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = menu)
    reboot.pack(padx = 10, pady = 10,ipadx=40, ipady=20)
    
def Producto(): 
    LimpiarVentana()
    prov = tkinter.Label(ventana, text = "PRODUCTO.",font=('Chiller 40 underline bold'), height=2, bg = 'cornflower blue')
    prov.pack()
    pbot1 = tkinter.Button(ventana, text = "Ingresar nuevo producto.", bg = "Light green", activebackground = "green", command = COMIDA)
    pbot1.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot2 = tkinter.Button(ventana, text = "Editar/actualizar producto.", bg = "Light green", activebackground = "green", command = COMIDA2)
    pbot2.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot6 = tkinter.Button(ventana, text = "Eliminar producto.", bg = "Light green", activebackground = "green", command = COMIDA3)
    pbot6.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot5 = tkinter.Button(ventana, text = "Ver productos.", bg = "Light green", activebackground = "green", command = COMIDA4)
    pbot5.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot3 = tkinter.Button(ventana, text = "Actualizar receta del producto.", bg = "Light green", activebackground = "green", command = COMIDA5)
    pbot3.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    pbot3 = tkinter.Button(ventana, text = "Categorías.", bg = "Light green", activebackground = "green", command = Categorias)
    pbot3.pack(padx = 10, pady = 10,ipadx=20, ipady=20)
    reboot = tkinter.Button(ventana, text = "Volver al menu.", bg = "Gray", command = menu)
    reboot.pack(padx = 10, pady = 10,ipadx=40, ipady=20)

def Salir():
    ventana.destroy()

def menu():
    LimpiarVentana()
    ventana['background'] = 'cornflower blue'
    titulo = tkinter.Label(ventana, text = "Sandwichería Fortiune",font=('Chiller 60 underline'), height=3, bg = 'cornflower blue')
    titulo.pack()
 
    bot1 = tkinter.Button(ventana, text = "PROVEEDOR", command = Proveedor, bg = "Light Blue", activebackground = "green")
    bot1.pack(padx = 20, pady = 20,ipadx=40, ipady=20)
    bot2 = tkinter.Button(ventana, text = "INVENTARIO", command = Inventario, bg = "Light Blue", activebackground = "green")
    bot2.pack(padx = 20, pady = 20,ipadx=40, ipady=20)
    bot2 = tkinter.Button(ventana, text = "PRODUCTO", command = Producto, bg = "Light Blue", activebackground = "green")
    bot2.pack(padx = 20, pady = 20,ipadx=40, ipady=20)
    salir = tkinter.Button(ventana, text = "SALIR", bg = "Red", command = Salir, activebackground = "Brown")
    salir.pack(padx = 20, pady = 20,ipadx=40, ipady=20)

menu()
ventana.mainloop()


