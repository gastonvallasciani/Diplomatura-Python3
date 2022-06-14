import os
import datetime
#------------------------------------------------------------------------------
__author__ = "Gastón Vallasciani"
__maintainter__ = "Gastón Vallasciani"
__email__ = "gastonvallasciani@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"
#------------------------------------------------------------------------------
class RegistroLogError(Exception):
    
    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "log_error.txt")

    def __init__(self, linea = 1, archivo = "ejemplo.py", fecha = datetime.datetime.now()):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha
    
    def registrar_log_error(self, linea, archivo, fecha):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha
        
        log = open(self.ruta, "a")
        print(f"Error detectado: " , self.archivo, self.linea, self.fecha, file=log)
#------------------------------------------------------------------------------
class RegistroLogEvento(Exception):

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "log_evento.txt")

    def __init__(self, fecha = datetime.datetime.now(), evento = "ERROR"):
        self.fecha = fecha
        self.evento = evento

    def registrar_log_evento(self, evento, fecha):
        self.fecha = fecha
        self.evento = evento
        log = open(self.ruta, "a")
        print(f"Evento: {self.evento}, Fecha: {self.fecha}", file=log)
#------------------------------------------------------------------------------
class RegistrarLog():
    def ejecutar_registro_log_error(self, linea, archivo, fecha):
        try:
            raise RegistroLogError()
        except RegistroLogError as log:
            log.registrar_log_error(linea, archivo, fecha)

    def ejecutar_registro_log_evento(self, evento, fecha):
        try:
            raise RegistroLogEvento()
        except RegistroLogEvento as log:
            log.registrar_log_evento(evento, fecha)    
#------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Version del modulo: ", __version__)
    print("Autor: ", __author__)

    objeto_registro = RegistrarLog()

    objeto_registro.ejecutar_registro_log_error(7, 'archivo1.txt', datetime.datetime.now())

    objeto_registro.ejecutar_registro_log_evento("Inicio de app", datetime.datetime.now())
#------------------------------------------------------------------------------
