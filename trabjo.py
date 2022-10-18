import sys


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def exponencial(a, b):
    return a**b


if __name__ == "__main__":

    while True:

        tipo = input("Que operaciòn desea hacer?").lower()
        if (
            tipo == "suma"
            or tipo == "resta"
            or tipo == "division"
            or tipo == "multiplicacion"
            or tipo == "exponencial"
            or tipo == "salir"
        ):
            if tipo == "salir":
                sys.exit()

            a = int(input("digite el numero 1:"))
            b = int(input("digite el numero 2:"))

            if tipo == "suma":
                resultado = suma(a, b)
                print(resultado)

            if tipo == "resta":

                resultado = resta(a, b)
                print(resultado)

            if tipo == "multiplicacion":

                resultado = multiplicacion(a, b)
                print(resultado)

            if tipo == "division":

                resultado = division(a, b)
                print(resultado)

            if tipo == "exponencial":

                resultado = exponencial(a, b)
                print(resultado)

        else:
            print("no escogio operacion")
