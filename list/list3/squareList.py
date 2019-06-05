"""Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista."""


def first_squares_list(number):
    array_list = []
    if number > 1:
        for x in range(1, number + 1):
            array_list.append(x ** 2)
    return array_list


def last_10_from_array(array_list):
    if len(array_list) > 10:
        start = len(array_list) -1
        for x in range(start, start - 10, -1):
            print(array_list[x])


if __name__ == '__main__':
    array_more_ten = first_squares_list(11)
    last_10_from_array(array_more_ten)
