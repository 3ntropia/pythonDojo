"""Generar dos listas con M y N números al azar entre 1 y 50 y construir una tercera
lista cuyos elementos sean el resultado de la intersección de las dos listas dadas.
Los valores de M y N se obtienen al azar. Imprimir las tres listas por pantalla."""
import random


def build_list(size):
    return [random.randint(1, 50) for x in range(size)]


def merge_list_naive(array_list_left, array_list_right):
    intersection = []
    for x in range(len(array_list_left)):
        for y in range(len(array_list_right)):
            if array_list_left[x] == array_list_right[y]:
                intersection.append(array_list_left[x])
    return


def merge_list_new(array_list_left, array_list_right):
    intersection = []
    for x in array_list_left:
        for y in array_list_right:
            if array_list_left.count(y) > 1:
                intersection.append(x)
    return


