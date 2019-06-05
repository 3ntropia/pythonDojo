"""" Escribir funciones para:
 a. Generar una lista de 50 números aleatorios del 1 al 100.
 b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido.
 La función no debe modificar la lista.
 c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
 únicos de la lista original, sin importar el orden.
 Combinar estas tres funciones en un mismo programa """
import random


def create_list():
    random_list = []
    for x in range(50):
        random_list.append(random.randint(1, 100))
    return random_list


def has_repeated_element(array_list):
    for x in range(len(array_list)):
        if array_list.count(array_list[x]) > 1:
            return True
    return False


def has_repeated_element_set(array_list):
    set_list = set(array_list)
    if len(set_list) == len(array_list):
        return False
    return True


def has_repeated_element_naive(array_list):
    for x in range(len(array_list)):
        for y in range(x + 1, len(array_list)):
            if array_list[x] == array_list[y]:
                return True
    return False


def unique_list_set(array_list):
    return list(set(array_list))


def unique_list_naive(array_list):
    array_list_copy = []
    for x in array_list:
        if array_list_copy.count(array_list[x]) == 0:
            array_list_copy.append(x)
    return array_list_copy
