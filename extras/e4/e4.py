"""Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento."""


def can_be_fit(domino1, domino2):
    if domino1[0] == domino2[0] or domino1[0] == domino2[1]:
        return True
    return domino1[1] == domino2[0] or domino1[1] == domino2[1]
