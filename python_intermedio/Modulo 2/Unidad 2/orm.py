"""
Ejemplo de uso de ORM PEEWEE con una base de datos SQLite3
"""

from peewee import *

# Selecciono la base de datos
db = SqliteDatabase("mi_base.db")

class  BaseModel(Model):
    class Meta:
        database = db

# creacion de la tabla
class Noticia(BaseModel):
    titulo = CharField(unique=True) # El parametro unique me permite agregar la restricción en la columna de que no pueden ingresarse dos titulos iguales en la base de datos.
    descripcion = CharField()

db.connect()
db.create_tables([Noticia])

class Abmc():
    def __init__(self):
        pass
    def alta(self, titulo, descripcion):
        noticia = Noticia()
        noticia.titulo = titulo
        noticia.descripcion = descripcion
        noticia.save()
    def seleccionar(self,):
        for fila in Noticia.select():
            print("ID: " + str(fila.id))
            print("Titulo: " + fila.titulo)
            print("Descripcion: " + fila.descripcion)
    def baja(self, id):
        borrar = Noticia.get(id)
        borrar.delete_instance()
    def modificacion(self, id, titulo, descripcion):
       # actualizar = Noticia.update((titulo, descripcion).where(Noticia.id==id))
       # actualizar.execute()
       pass

if __name__ == "__main__":
    print("Prueba de ORM con SQLite3")
    abmc = Abmc()
    try:
        abmc.alta("Titulo1", "Descripcion1")
    except:
        print("El registro que estas tratando de dar de alta ya esta dado de alta en la base de datos")
    abmc.seleccionar()
    try:
        abmc.baja(3)
    except:
        print("El registro que estas tratando de borrar no existe en la base de datos")
    try:
        abmc.modificacion(2, "Titulo100", "Descripcion100")
    except:
        print("El registro que estas tratando de actualizar ya esta dado de alta en la base de datos")