"""Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando
éste sea correcto. Escribir también un programa que permita probar el correcto
funcionamiento de la misma."""


def print_if_valid_number(number):
    if not number.isnumeric():
        raise ValueError('Must input a number. The value of X was: {}'.format(number))
    if int(number) <= 0:
        raise ValueError('X should be positive. The value of X was: {}'.format(number))
    print(number)


def input_number():
    number = input("Type a number for X: ")
    print_if_valid_number(number)


if __name__ == '__main__':
    input_number()
