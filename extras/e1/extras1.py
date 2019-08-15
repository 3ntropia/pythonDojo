"""Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa para verificar su comportamiento:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas."""

from functions.function2 import validDate
from functions.function9 import operateDate


def input_valid_date():
    day = int(input("dia:"))
    month = int(input("mont:"))
    year = int(input("year:"))
    date = (day, month, year)
    return validDate.is_date_valid(date[0], date[1], date[2])


def add_days(n, date):
    (day, month, year) = operateDate.add_n_days(date[0], date[1], date[2], n)
    print(date(day, month, year))

