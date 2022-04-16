from programa_a_testear import sumar
from programa_a_testear import multiplicar
import pytest

# Decorador skip de pytest: evita que se testee esta funcion
#@pytest.mark.skip(reason="no way of currently testing this")

@pytest.mark.marca1
def test_sumar_incorrecto():
    assert sumar(1, 2)==7

@pytest.mark.skip(reason="no way of currently testing this")
def test_sumar_correcto():
    assert sumar(1, 2)==3