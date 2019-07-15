"""Desarrollar una función que devuelva el producto de dos números enteros por su-
mas sucesivas."""


def multiplication(base, times, index=1):
    if index == times:
        return base
    else:
        return base + multiplication(base, times, index + 1)
