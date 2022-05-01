from pickle import FALSE
from pickle import TRUE
import re

class DataValidationManager():
    def __init__(self) -> None:
        pass

    def validar_letras(self, cadena_a_validar):
        patron = re.compile("[a-zA-Z áéíóú]")

        if patron.match(cadena_a_validar) == None:
            return FALSE
        else:
            return TRUE

    def validar_numeros(self, cadena_a_validar):
        patron_numeros = re.compile("[1-9][0-9]{0,1}")

        if patron_numeros.match(cadena_a_validar) == None:
            return FALSE
        else:
            return TRUE

    def validar_fecha(self, cadena_a_validar):
        patron_fecha = re.compile("^[\d]{4}-[\d]{2}-[\d]{2}$")
        
        if patron_fecha.match(cadena_a_validar) == None:
            return FALSE
        else:
            return TRUE