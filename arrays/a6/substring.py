"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento
de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes
casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""


def slicing(string, first, last):
    return string[first:last]


def substring_slicing(string, first, n):
    return slicing(string, first, first + n)


def not_slicing(string, first, last):
    result = ""
    for i in range(len(string)):
        if first <= i < last:
            result += string[i]
    return result


def substring_not_slicing(string, first, n):
    return not_slicing(string, first, first + n)
