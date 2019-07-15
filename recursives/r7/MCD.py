"""Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo Común Divisor
 (también llamado Divisor Común Mayor) basándose en las siguientes propiedades:

MCD(X, X) = X
MCD(X, Y) = MCD(Y, X)
Si X > Y => MCD(X, Y) = MCD(X–Y, Y).

Utilizando la función anterior calcular el MCD de todos los elementos de una lista
de números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite utilizar
 iteraciones en ninguna etapa del proceso."""


#with loop
def mcd(x, y):
    maximum = max(x, y)
    for numbers in range(maximum, 1, -1):
        if x % maximum == 0 and y % maximum == 0:
            return maximum


def mcd_recursive(x, y, maximum):
    if x % maximum == 0 and y % maximum == 0:
        return maximum
    else:
        return mcd_recursive(x, y, maximum - 1)


def mcd_non_loop(x, y):
    return mcd_recursive(x, y, max(x, y))


def mcd_list(list, index=0):
    if index == len(list):
        return mcd_non_loop(list[index], list[index + 1])
    else:
        return mcd_list(mcd_non_loop(list[index]))