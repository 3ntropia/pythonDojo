"""
Realizar una función que reciba como parámetros dos cadenas de caracteres con-
teniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""


def join_number(str_integer, str_float):
    if not str_integer.isnumeric():
        raise ValueError("Must enter a number")
    if not str_float.isnumeric():
        raise ValueError("Must enter a number")
    return str_integer + "," + str_float


def handle_exception():
    str_integer = input("Ingrese la parte entera: ")
    str_float = input("Ingrese la parte flotante: ")
    try:
        return join_number(str_integer, str_float)
    except ValueError:
        return -1


if __name__ == '__main__':
    print(handle_exception())
