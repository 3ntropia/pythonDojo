"""Escribir un programa que permita ingresar una cadena de caracteres e imprima un
mensaje indicando cuántas letras y cuántos números contiene. Por ejemplo, si se
ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3 números."""

def count_char_numbers(string):
    numbers = 0
    chars = 0
    for char in string:
        if char.isdigit():
            numbers += 1
        else:
            chars += 1
    return numbers, chars
