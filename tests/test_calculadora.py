import pytest

from src.calculadora import dividir, fatorial, multiplicar, potencia, raiz_quadrada, somar, subtrair


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


def test_fatorial_caso_base():
    assert fatorial(0) == 1


def test_fatorial_recursivo():
    assert fatorial(5) == 120


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-1)


def test_raiz_quadrada():
    assert raiz_quadrada(4) == 2.0
    assert raiz_quadrada(0) == 0.0
    assert raiz_quadrada(2) == pytest.approx(1.4142135623730951)


def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-1)
