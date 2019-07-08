"""La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo."""
from math import sqrt


def sqrt_function(number):
    if number < 0:
        raise ValueError("Number should be positive")
    return sqrt(number)


if __name__ == '__main__':
    print(sqrt_function(-2))
