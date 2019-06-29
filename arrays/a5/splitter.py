"""Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo
una frase y un entero N, y devuelva otra cadena con las palabras que tengan
N o más caracteres de la cadena original. Escribir también un programa para
verificar el comportamiento de la misma. Hacer tres versiones de la función, para
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter"""


def filter_word_len_v1(string, number):
    split_list = string.split()
    result = ""
    for x in split_list:
        if len(x) >= number:
            result += x + " "
    return result[:-1]


def filter_word_len_v2(string, number):
    split_list = string.split()
    result = [x for x in split_list if len(x) >= number]
    return result


def filter_word_len_v3(string, number):
    split_list = string.split()
    result = list(filter(lambda x: len(x) >= number, split_list))
    return result


