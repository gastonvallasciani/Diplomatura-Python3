import mysql.connector
import re

class Mysql_database():
    def __init__(self):
        pass

    def crear_base_mysql(self, nombre_base):
        self.mibase = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd=""
        )
        self.micursor = self.mibase.cursor()
        data = f"CREATE DATABASE {nombre_base}"
        self.micursor.execute(data)

    def crear_tabla_mysql(self, nombre_base):
        self.mibase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=nombre_base
        )
        self.micursor = self.mibase.cursor()
        self.micursor.execute("CREATE TABLE productos(id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, producto VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, cantidad REAL COLLATE utf8_spanish2_ci NOT NULL, precio REAL COLLATE utf8_spanish2_ci NOT NULL)")

    def alta_mysql(self, nombre_base, producto, cantidad, precio, tree):
        cadena = producto
        patron="^[A-Za-záéíóú]*$"  #regex para el campo cadena
        
        if(re.match(patron, cadena)):
            print(producto, cantidad, precio)
            self.mibase = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database=nombre_base
            )
            self.micursor = self.mibase.cursor()
            data=(producto, cantidad, precio)
            sql = "INSERT INTO productos (producto, cantidad, precio) VALUES (%s, %s, %s)"
            data =(producto, cantidad, precio)
            self.micursor.execute(sql, data)
            self.mibase.commit()
            print(self.micursor.rowcount, "Cantidad de registros agregados.")
            print("Estoy en alta todo ok")
            self.actualizar_treeview_mysql(nombre_base, tree)
        else:
            print("error en campo producto")

    def baja_mysql(self, nombre_base):
        self.mibase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=nombre_base
        )
        self.micursor = self.mibase.cursor()
        sql = "DELETE FROM productos WHERE id=%s"
        datos = ('1',)

        self.micursor.execute(sql, datos)
        self.mibase.commit()
        print(self.micursor.rowcount, "Registro borrado")

    def actualizar_treeview_mysql(self, nombre_base, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        mibase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=nombre_base
        )
        micursor = mibase.cursor()
        sql = "SELECT * FROM productos"
        micursor.execute(sql)
        resultado = micursor.fetchall()

        for fila in resultado:
            print(fila)
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))


if __name__=="__main__":
    objeto_database = Mysql_database()
    nombre_base_nueva = "base_nueva"
    try:
        objeto_database.crear_base_mysql(nombre_base_nueva)
        objeto_database.crear_tabla_mysql(nombre_base_nueva)
    except:
        print("Error: Database and table already created")