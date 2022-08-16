import sqlite3

# crear tabla

def crearTabla():
    conexion = sqlite3.connect("basededatos.db")
    consulta = conexion.cursor()
    sql = """CREATE TABLE IF NOT EXISTS agenda (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre VARCHAR(20) NOT NULL, apellido VARCHAR(20) NOT NULL, telefono VARCHAR(14) NOT NULL,
    email VARCHAR(20) NOT NULL)"""
    if (consulta.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")
    conexion.close()

# insertar Datos

def inserta(nombre, apellido, telefono, email):
    conexion = sqlite3.connect("basededatos.db")
    consulta = conexion.cursor()
    datos = (nombre, apellido, telefono, email)
    sql = """INSERT INTO agenda(nombre, apellido, telefono, email) VALUES (?,?,?,?)"""
    if (consulta.execute(sql, datos)):
        print("Se ha insertado")
    else:
        print("No se ha insertado datos")
    conexion.commit()
    conexion.close()