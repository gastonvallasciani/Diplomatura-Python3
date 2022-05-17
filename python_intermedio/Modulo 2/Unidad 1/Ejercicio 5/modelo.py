from sqlite3_mod import Sqlite3_database
from mysql_mod import Mysql_database
# ##############################################
# MODELO
# ##############################################
class Database():
    def __init__(self, database_name="BASE_DEFAULT", database_type="SQlite3"):
        self.database_name = database_name
        self.database_type = database_type
        self.objecto_sqlite3 = Sqlite3_database()
        self.objeto_mysql = Mysql_database()

    def configurar_database(self, database_name, database_type):
        self.database_name = database_name
        self.database_type = database_type
        print(f"new_database_name: {self.database_name}")
        print(f"new_database_type: {self.database_type}")

    def imprimir_atributos_por_consola(self,):
        print(f"database_name: {self.database_name}")
        print(f"database_type: {self.database_type}")

    def iniciar_database(self,):
        if self.database_type == "SQlite3":
            try:
                self.objecto_sqlite3.conexion_sqlite3(self.database_name)
                self.objecto_sqlite3.crear_tabla_sqlite3(self.database_name)
            except:
                print("Error")
        elif self.database_type == "MySQL":
            try:
                self.objeto_mysql.crear_base_mysql(self.database_name)
                self.objeto_mysql.crear_tabla_mysql(self.database_name)
            except:
                print("Error")

    def alta(self, nombre_base, producto, cantidad, precio, tree):
        if self.database_type == "SQlite3":
            self.objecto_sqlite3.alta_sqlite3(nombre_base, producto, cantidad, precio, tree)
        elif self.database_type == "MySQL":
            self.objeto_mysql.alta_mysql(nombre_base, producto, cantidad, precio, tree)

    def actualizar_treeview(self, nombre_base, mitreview):
        if self.database_type == "SQlite3":
            self.objecto_sqlite3.actualizar_treeview_sqlite3(nombre_base, mitreview)
        elif self.database_type == "MySQL":
            self.objeto_mysql.actualizar_treeview_mysql(nombre_base, mitreview)
        
class Abmc(Database):
    def __init__(self, database_name="BASE_DEFAULT", database_type="SQlite3"):
        super(Abmc, self).__init__(database_name, database_type)
        
        
if __name__=="__main__":
    objeto_database = Database()
    objeto_database.imprimir_atributos_por_consola()

    objeto_abmc = Abmc()
    objeto_abmc.imprimir_atributos_por_consola()


"""
    def consultar():
        global compra
        print(compra)

def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']

    con=conexion()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM productos WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)

"""



