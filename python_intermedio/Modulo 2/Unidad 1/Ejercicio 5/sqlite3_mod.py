import sqlite3
import re

class Sqlite3_database():
    def __init__(self):
        pass
    
    def conexion_sqlite3(self, nombre_base):
        con = sqlite3.connect(f"{nombre_base}.db")
        return con

    def crear_tabla_sqlite3(self, nombre_base):
        con = self.conexion_sqlite3(nombre_base)
        cursor = con.cursor()
        sql = """CREATE TABLE productos
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto varchar(20) NOT NULL,
                cantidad real,
                precio real)
        """
        cursor.execute(sql)
        con.commit()

    def alta_sqlite3(self, nombre_base, producto, cantidad, precio, tree):
        cadena = producto
        patron="^[A-Za-záéíóú]*$"  #regex para el campo cadena
        if(re.match(patron, cadena)):
            print(producto, cantidad, precio)
            con=self.conexion_sqlite3(nombre_base)
            cursor=con.cursor()
            data=(producto, cantidad, precio)
            sql="INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
            cursor.execute(sql, data)
            con.commit()
            print("Estoy en alta todo ok")
            self.actualizar_treeview_sqlite3(nombre_base, tree)
        else:
            print("error en campo producto")

    def actualizar_treeview_sqlite3(self, nombre_base, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        sql = "SELECT * FROM productos ORDER BY id ASC"
        con=self.conexion_sqlite3(nombre_base)
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))