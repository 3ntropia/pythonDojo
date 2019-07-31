"""Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de Octubre de
2017". Escribir también un programa para verificar su comportamiento."""

months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"
          "Octubre", "Noviembre", "Diciembre")


def split_tuple(date):
    day = date[0]
    month = date[1]
    year = date[2]
    return str(day) + " " + months[month - 1] + " " + str(year)


if __name__ == '__main__':
    print(split_tuple((1, 2, 2010)))
