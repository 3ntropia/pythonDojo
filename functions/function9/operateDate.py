"""
Escribir una funcion diasiguiente(…) que reciba como parametro una fecha cualquiera
 expresada por tres enteros (correspondientes al día, mes y año) y calcule y
 devuelva tres enteros correspondientes el día siguiente al dado.
 Utilizando esta funcion, desarrollar programas que permitan:
 a. Sumar N dias a una fecha.
 b. Calcular la cantidad de dias existentes entre dos fechas cualesquiera.
"""
from functions.function2 import validDate


def next_date(day, month, year):
    if validDate.is_date_valid(day, month, year):
        day += 1
        if day > 28 and month == 2:
            if not validDate.is_leap_year(year):
                day = 1
                month += 1
        if day == 31:
            if month == 2 or month == 4 or month == 6 or month == 8 or month == 10:
                day = 1
                month += 1
        elif day > 31:
            day = 1
            month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year


def add_n_days(day, month, year, number):
    for x in range(number):
        (day, month, year) = next_date(day, month, year)
    return day, month, year


def diff_dates(day, month, year, day2, month2, year2):
    counter = 0
    while day != day2 or month != month2 or year != year2:
        (day, month, year) = next_date(day, month, year)
        counter += 1
    return counter
