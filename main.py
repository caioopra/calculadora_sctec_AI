from src.calculadora import somar, subtrair, multiplicar, dividir, potencia


def main():
    print("Calculadora")
    print(f"2 + 3 = {somar(2, 3)}")
    print(f"5 - 1 = {subtrair(5, 1)}")
    print(f"4 * 2 = {multiplicar(4, 2)}")
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"2 ^ 8 = {potencia(2, 8)}")


if __name__ == "__main__":
    main()
