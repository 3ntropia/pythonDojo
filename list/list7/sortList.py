"""Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función."""


def is_sorted(array_list):
    array_list_copy = list(array_list)
    array_list_copy.sort()
    for x in range(len(array_list)):
        if array_list[x] != array_list_copy[x]:
            return False
    return True
