from tkinter import *
from baseDatosSqlite import *
from tkinter import messagebox

listado=[]

# funcion prueba

def mostrar():
    print("Esto es una prueba")

# funciones

def mensaje(titulo, texto):
    messagebox.showinfo(titulo, texto)

def listar():
    if (len(listado) > 0):
        # borrar lista
        listado.clear()
    conexion = sqlite3.connect("basededatos.db")
    consulta = conexion.cursor()
    consulta.execute("SELECT id, nombre, apellido, telefono, email from agenda")
    for i in consulta:
        id = (i[0])
        nombre = (i[1])
        apellido = (i[2])
        telefono = (i[3])
        email = (i[4])
        listado.append(i)
        listado.sort()
    conexion.close()
    try:
        text_box.delete(0, END)
    except:
        mensaje("Listado", "Error en listado")
    text_box.insert(INSERT, "id\tNombre\t\tApellido\t\tTelefono\n")
    for elemento in listado:
        id = elemento[0]
        nombre = elemento[1]
        apellido = elemento[2]
        telefono = elemento[3]
        text_box.insert(INSERT, id)
        text_box.insert(INSERT, "\t")
        text_box.insert(INSERT, nombre)
        text_box.insert(INSERT, "\t")
        text_box.insert(INSERT, "\t")
        text_box.insert(INSERT, apellido)
        text_box.insert(INSERT, "\t")
        text_box.insert(INSERT, "\t")
        text_box.insert(INSERT, telefono)
        text_box.insert(INSERT, "\t")
        text_box.insert(INSERT, "\n")

def limpiar():
    ID.set("")
    nombre.set("")
    apellido.set("")
    telefono.set("")
    email.set("")

def guardar():
    no = nombre.get()
    ap = apellido.get()
    te = telefono.get()
    em = email.get()
    if ((no=="") or (ap=="")):
        print("Faltan datos")
    else:
        limpiar()
        crearTabla()
        inserta(no, ap, te, em)
        print("Datos guardados")
    listar()


window = Tk()
window.config(bg="blue")
window.geometry("560x540")
window.title("Agenda")
frame = Frame()
frame.config(width=560, height=540)
frame.config(bg="blue")
frame.pack()

# variables

ID = IntVar()
nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
email = StringVar()

# Widgets

id_label = Label(frame, text="ID: ").place(x=50, y=50)
id_entry = Entry(frame, textvariable=ID).place(x=130, y=50)
name_label = Label(frame, text="Name: ").place(x=50, y=90)
name_entry = Entry(frame, textvariable=nombre).place(x=130, y=90)
surname_label = Label(frame, text="Surname: ").place(x=50, y=130)
surname_entry = Entry(frame, textvariable=apellido).place(x=130, y=130)
phone_label = Label(frame, text="Phone: ").place(x=50, y=170)
phone_entry = Entry(frame, textvariable=telefono).place(x=130, y=170)
email_label = Label(frame, text="Email: ").place(x=50, y=210)
email_entry = Entry(frame, textvariable=email).place(x=130, y=210)
text_box = Text(frame)
text_box.place(x=50, y=240, width=500, height=200)

# buttons

add_button = Button(frame, text="Add", command=guardar).place(x=150, y=500)
delete_button = Button(frame, text="Delete", command=mostrar).place(x=200, y=500)
search_button = Button(frame, text="Search", command=mostrar).place(x=250, y=500)
update_button = Button(frame, text="Update", command=mostrar).place(x=320, y=500)
window.mainloop()