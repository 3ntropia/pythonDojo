"""Escribir una función que devuelva la suma de los N primeros números naturales."""


def recursive(number, counter=0, sum=0):
    if number == counter:
        return sum
    else:
        counter += 1
        return recursive(number, counter, sum + counter)


def summation(number):
    return recursive(number)
