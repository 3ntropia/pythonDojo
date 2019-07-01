"""Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""


def remove_slicing(string, first, last):
    return string[:first] + string[last:]


def remove_substring(string, first, number):
    return remove_slicing(string, first, first + number)


def remove_not_slicing(string, first, last):
    result = ""
    for i in range(len(string)):
        if i < first or i >= last:
            result += string[i]
    return result


def remove_substring_not_slicing(string, first, number):
    return remove_not_slicing(string, first, first + number)


