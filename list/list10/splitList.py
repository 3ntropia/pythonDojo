"""Generar una lista con números al azar entre 0 y 100, donde su cantidad de elementos
será un número par también obtenido al azar entre 10 y 50. Luego se solicita
partir la lista por la mitad a través de la técnica de las rebanadas, creando dos
nuevas listas. Imprimir las tres listas por pantalla."""
from list.list8 import mergeList
import random


def split(array_list):
    return array_list[:int(len(array_list)/2)], array_list[int(len(array_list)/2):]


def build_array():
    even_list = [x for x in range(10, 50, 2)]
    x = random.sample(even_list, 1)
    return mergeList.build_list(x[0])


if __name__ == "__main__":
    random_list = build_array()
    print(random_list)
    (first_list, second_list) = split(random_list)
    print(first_list)
    print(second_list)
