"""Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros."""


def last_values(string, number):
    return string[len(string) - number:]
