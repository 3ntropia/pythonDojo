"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones."""


def get_month(number):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December"]
    if number > 12 or number < 0:
        raise ValueError("Month out of range")
    return months[number - 1]


if __name__ == '__main__':
    #get_month(13)
    print(get_month(11))
