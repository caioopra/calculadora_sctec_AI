import pytest

from src.calculadora import celsius_para_fahrenheit, dividir, fatorial, multiplicar, potencia, somar, subtrair


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


def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(-40) == -40


def test_celsius_para_fahrenheit_tipo_invalido():
    with pytest.raises(TypeError):
        celsius_para_fahrenheit("quente")
