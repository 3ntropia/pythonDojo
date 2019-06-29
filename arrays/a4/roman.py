"""Escribir una función que reciba como parámetro un número entero entre 0 y 3999
y lo convierta en un número romano, devolviéndolo en una cadena de caracteres.
¿En qué cambiaría la función si el rango de valores fuese diferente?"""

__INT_THOUSANDS__ = 1000
__INT_HUNDREDS__ = 100
__INT_TENS__ = 10


def roman_converter(number):
    units = [0, 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = [0, 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XL']
    hundreds = [0, 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = [0, 'M', 'MM', 'MMM']
    roman = ""
    int_thousand = int(number / __INT_THOUSANDS__)
    if int_thousand > 0:
        roman += thousands[int_thousand]
        number -= int_thousand * __INT_THOUSANDS__
    int_hundred = int(number / __INT_HUNDREDS__)
    if int_hundred > 0:
        roman += hundreds[int_hundred]
        number -= int_hundred * __INT_HUNDREDS__
    int_ten = int(number / __INT_TENS__)
    if int_ten > 0:
        roman += tens[int_ten]
        number -= int_ten * __INT_TENS__
    if number > 0:
        roman += units[number]
    return roman
