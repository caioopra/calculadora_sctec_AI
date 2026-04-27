import pytest

from src.calculadora import dividir, multiplicar, potencia, somar, subtrair


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_subtrair():
    assert subtrair(5, 1) == 4
    assert subtrair(0, 7) == -7


def test_multiplicar():
    assert multiplicar(4, 2) == 8
    assert multiplicar(-3, 3) == -9
    assert multiplicar(0, 99) == 0


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(1, 0)


def test_potencia():
    assert potencia(2, 8) == 256
    assert potencia(5, 0) == 1
    assert potencia(2, -1) == 0.5
