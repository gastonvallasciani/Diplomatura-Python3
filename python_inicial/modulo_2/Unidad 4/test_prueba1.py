from programa_a_testear import sumar
from programa_a_testear import multiplicar
import pytest

def test_sumar_incorrecto():
    assert sumar(1, 2)==7

def test_sumar_correcto():
    assert sumar(1, 2)==3