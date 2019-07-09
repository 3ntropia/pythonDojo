"""Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
utilizar cadenas de caracteres."""


def digit_counter(index, counter, integer):
    counter += 1
    index += 1
    if len(str(integer)) == index:
        return counter
    else:
        return digit_counter(index, counter, integer)
