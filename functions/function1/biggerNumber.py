"""Desarrollar una función que reciba tres números positivos y devuelva el mayor de
los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto
devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también
un programa para ingresar los tres valores, invocar a la función y mostrar el
máximo hallado, o un mensaje informativo si éste no existe."""


def bigger(a, b, c):
    if a > b:
        if a > c:
            return str(a)
    if b > a:
        if b > c:
            return str(b)
    if c > a:
        if c > b:
            return str(c)
    return "No hay mayores"
