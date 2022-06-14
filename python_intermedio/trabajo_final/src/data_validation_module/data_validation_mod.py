"""
data_validation_mod.py

Modulo utilizado para llevar a cabo la validacion de datos.
"""
from pickle import FALSE
from pickle import TRUE
import re
#------------------------------------------------------------------------------
__author__ = "Gastón Vallasciani"
__maintainter__ = "Gastón Vallasciani"
__email__ = "gastonvallasciani@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"
#------------------------------------------------------------------------------
class DataValidationManager():
    def __init__(self):
        pass

    def validar_letras(self, cadena_a_validar):
        """
        Metodo para validar letras en strings
        
        :cadena_a_validar: Cadena a verificar si se encuentra conformada solo por letras.

        :returns: FALSE = ERROR AL VALIDAR, TRUE = OK
        """
        patron = re.compile("[a-zA-Z áéíóú]")

        if patron.match(cadena_a_validar) == None:
            return FALSE
        else:
            return TRUE

    def validar_numeros(self, cadena_a_validar):
        """
        Metodo para validar numeros en strings
        
        :cadena_a_validar: Cadena a verificar si se encuentra conformada solo por numeros.

        :returns: FALSE = ERROR AL VALIDAR, TRUE = OK
        """
        patron_numeros = re.compile("[1-9][0-9]{0,1}")

        if patron_numeros.match(cadena_a_validar) == None:
            return FALSE
        else:
            return TRUE

    def validar_fecha(self, cadena_a_validar):
        """
        Metodo para validar fechas en strings

        Formato de fecha: AAAA-MM-DD
        
        :cadena_a_validar: Cadena a verificar si tiene el formato de una fecha.

        :returns: FALSE = ERROR AL VALIDAR, TRUE = OK
        """
        patron_fecha = re.compile("^[\d]{4}-[\d]{2}-[\d]{2}$")
        
        if patron_fecha.match(cadena_a_validar) == None:
            return FALSE
        else:
            return TRUE
#------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Version del modulo: ", __version__)
    print("Autor: ", __author__)
#------------------------------------------------------------------------------