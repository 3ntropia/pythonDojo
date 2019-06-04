"""" Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento
 imprimiendo la lista luego de invocar a cada función:
 a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al
  azar de dos dígitos.
 b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
 c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y
 la función lo recibe como parámetro.
 d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas  auxiliares.
  Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]."""
import random


def create_list():
    random_list = []
    length = random.randint(10, 99)
    for x in range(0, length):
        random_list.append(random.randint(1000, 9999))
    return random_list


def sum_list(random_list):
    sum = 0
    for x in random_list:
        sum += random_list[x]
    return sum


def remove_from_list(random_list, value):
    while value in random_list:
        random_list.remove(value)
    return random_list


# WIP
def remove_from_list_old_school(random_list, value):
    back_up_list = random_list
    for x in random_list:
        if random_list[x] == value:
            back_up_list = manual_remove(random_list, x)
    return back_up_list


def manual_remove(array_list, position):
    for x in range(position, len(array_list) - 1):
        array_list[x] = array_list[x + 1]
    return array_list


def is_palindrome(random_list):
    for x in range(0, len(random_list / 2)):
        if random_list[x] != random_list[len(random_list) - 1]:
            return False
    return True


if __name__ == '__main__':
    array_list = create_list()
    print(array_list)