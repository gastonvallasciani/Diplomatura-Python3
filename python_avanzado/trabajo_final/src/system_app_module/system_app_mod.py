
#------------------------------------------------------------------------------
__author__ = "Gastón Vallasciani"
__maintainter__ = "Gastón Vallasciani"
__email__ = "gastonvallasciani@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"
#------------------------------------------------------------------------------
class SystemApp():
    def __init__(self, app_version, inicio):
        self.version = app_version
        self.inicio = inicio
    def __str__(self,):
        return("Clase SystemApp()")
#------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Version del modulo: ", __version__)
    print("Autor: ", __author__)
#------------------------------------------------------------------------------