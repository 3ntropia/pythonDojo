"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares. Escribir además un programa que permita verificar su
funcionamiento."""


def is_palindrome(random_list):
    for x in range(int(len(random_list) / 2)):
        if random_list[x] != random_list[len(random_list) - x - 1]:
            return False
    return True


