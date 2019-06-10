"""Escribir un programa para generar una lista con los múltiplos de 7 que no sean
múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida."""


def multiple_seven():
    array_numbers = []
    for x in range(2000, 3500, 7):
        if x % 5 != 0:
            array_numbers.append(x)
    return array_numbers


if __name__ == '__main__':
    print(multiple_seven())
