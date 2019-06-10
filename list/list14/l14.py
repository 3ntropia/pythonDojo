"""Escribir un programa para generar una lista con los múltiplos de 7 que no sean
múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida.
Repetir el ejercicio anterior, pero utilizando la técnica de listas por comprensión."""


def multiple_seven():
    return [x for x in range(2000, 3500, 7) if x % 5 != 0]


if __name__ == '__main__':
    print(multiple_seven())
