import os
import datetime

class RegistroLog(Exception):

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "log.txt")

    def __init__(self, linea, archivo, fecha):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha
    
    def registrar_log_error(self):
        log = open(self.ruta, "a")
        print("Error: ", self.archivo, self.linea, self.fecha, file=log)

    def registrar_log_evento(self, evento):
        log = open(self.ruta, "a")
        print("Evento: ", evento, self.fecha, file=log)


if __name__ == "__main__":
    def registrar():
        raise RegistroLog(7, 'archivo1.txt', datetime.datetime.now())

    def registrar_evento():
        raise RegistroLog(7, 'archivo1.txt', datetime.datetime.now()) 

    try:
        registrar()
    except RegistroLog as log:
        log.registrar_log_error()

    try:
        registrar_evento()
    except RegistroLog as log:
        log.registrar_log_evento("Inicio de app")

