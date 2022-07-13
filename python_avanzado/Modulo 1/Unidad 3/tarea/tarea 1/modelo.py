import sqlite3
from peewee import *

# Declaracion de funcion decoradora
def decorador_ingreso_nuevo_registro(funcion):
    def envoltura(*args):
        print("Se ha ingresado un nuevo registro")
        funcion(*args)
    return envoltura

# Declaracion de funcion decoradora
def decorador_eliminacion_de_registro(funcion):
    def envoltura(*args):
        print("Se ha eliminado el registro")
        funcion(*args)
    return envoltura

# Declaracion de funcion decoradora
def decorador_actualizacion_de_registro(funcion):
    def envoltura(*args):
        print("Se ha actualizado el registro")
        funcion(*args)
    return envoltura

db = SqliteDatabase("mi_base.db")

class BaseModel(Model):
    class Meta:
        database = db

class Noticia(BaseModel):
    titulo = CharField(unique=True)
    descripcion = CharField()

    def __str__(self,):
        return "El título es: "+self.titulo+" con descripción: "+self.descripcion


db.connect()
db.create_tables([Noticia])


class Abmc:
    def __init__(
        self,
    ): pass
    
    @decorador_ingreso_nuevo_registro
    def alta(self, titulo, descripcion, mitreeview):
        noticia=Noticia()
        noticia.titulo=titulo.get()
        noticia.descripcion=descripcion.get()
        noticia.save()

        self.actualizar_treeview(mitreeview)

    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        # Consiguiendo datos
        for fila in Noticia.select():
            mitreeview.insert("", 0, text=fila.id, values=(fila.titulo, fila.descripcion, fila))

    @decorador_eliminacion_de_registro
    def baja(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        borrar=Noticia.get(Noticia.id==valor_id["text"])
        borrar.delete_instance()
        self.actualizar_treeview(mitreeview)

    @decorador_actualizacion_de_registro
    def modificar(self, titulo, descripcion, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        actualizar=Noticia.update(titulo=titulo.get(), descripcion=descripcion.get()).where(Noticia.id==valor_id["text"])
        actualizar.execute()
        self.actualizar_treeview(mitreeview)
