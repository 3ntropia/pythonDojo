"""Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal."""


def binarty_to_decimal(binary, level=0, sum =0):
    level += 1
    sum += 2 ** (level-1) * int(binary[-level])
    if level == len(binary):
        return sum
    else:
        return binarty_to_decimal(binary, level, sum)


