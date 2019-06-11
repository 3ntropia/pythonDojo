"""Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con
los elementos de la primera que sean impares. El proceso deberá realizarse utilizando
listas por comprensión. Imprimir las dos listas por pantalla."""
import random


def build_array(array_list):
    return [x for x in array_list if x % 2 != 0]


if __name__ == '__main__':
    r = [random.randint(1, 100) for _ in range(30)]
    print(r)
    print(build_array(r))
