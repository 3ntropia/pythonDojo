"""Escribir una función que reciba como parámetro una cadena de caracteres en la
que las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada
una."""


def sort_string(string):
    split_list = string.split()
    split_list.sort()
    result = ""
    for char in split_list:
        result += char + " "
    return result[:-1]

