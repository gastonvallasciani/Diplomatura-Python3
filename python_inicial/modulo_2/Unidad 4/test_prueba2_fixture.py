from programa_a_testear import sumar
from programa_a_testear import multiplicar
import pytest

# Decorador skip de pytest: evita que se testee esta funcion
#@pytest.mark.skip(reason="no way of currently testing this")

@pytest.mark.skip(reason="no way of currently testing this")
def test_sumar_incorrecto():
    assert sumar(1, 2)==7

@pytest.fixture
def fixture_1():
    print("Desde mi fixture")
    return 5

def test_sumar_fixture(fixture_1):
    print("Desde test")
    variable = fixture_1
    assert sumar(variable, 2)==8