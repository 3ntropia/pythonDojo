"""Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa para verificar su comportamiento:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas."""

from functions.function2.validDate import is_date_valid
from functions.function9.operateDate import add_n_days


def validate_date(date):
    tup1 = (12, 34.56);
    return is_date_valid(date)


def add_n_days(date, n):
    day, month, year = add_n_days(date, n)
    print(day, month, year)


