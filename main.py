from src.calculadora import dividir, fatorial, media, multiplicar, potencia, somar, subtrair


def main():
    print("Calculadora")
    print(f"2 + 3 = {somar(2, 3)}")
    print(f"5 - 1 = {subtrair(5, 1)}")
    print(f"4 * 2 = {multiplicar(4, 2)}")
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"2 ^ 8 = {potencia(2, 8)}")
    print(f"media de [2, 4, 6] = {media([2, 4, 6])}")
    print(f"5! = {fatorial(5)}")


if __name__ == "__main__":
    main()
