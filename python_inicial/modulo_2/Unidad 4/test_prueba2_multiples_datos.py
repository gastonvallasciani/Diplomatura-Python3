from programa_a_testear import sumar
from programa_a_testear import multiplicar
import pytest

# Decorador skip de pytest: evita que se testee esta funcion
#@pytest.mark.skip(reason="no way of currently testing this")

@pytest.mark.skip(reason="no way of currently testing this")
def test_sumar_incorrecto():
    assert sumar(1, 2)==7

@pytest.mark.parametrize(
    "a, b, resultado",
    [
        (1, 2, 3),
        (sumar(1, 2), 3, 6),
        (1, 2, 6),
        (3, 3, 6),
    ]
)
def test_sumar(a, b, resultado):
    assert sumar(a, b)==resultado