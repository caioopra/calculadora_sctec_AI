def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def potencia(base, expoente):
    return base ** expoente


def fatorial(n):
    if n < 0:
        raise ValueError("Não é possível calcular fatorial de número negativo")
    if n == 0:
        return 1
    return n * fatorial(n - 1)


def celsius_para_fahrenheit(c):
    if not isinstance(c, (int, float)):
        raise TypeError("A temperatura deve ser um número")
    return c * 9 / 5 + 32
