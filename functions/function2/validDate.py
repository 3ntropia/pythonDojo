# Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
# según la fecha sea correcta o no. Realizar también un programa para verificar el
# comportamiento de la función.

MAX_YEAR = 2050
MIN_YEAR = 1900


def is_date_valid(day, month, year):
    if 1 > day or day > 31:
        return False
    elif month == 4 or month == 6 or month == 8 or month == 10:
        if day > 30:
            return False
    elif month == 2:
        if is_leap_year(year):
            if day != 29:
                return False
        else:
            if day != 28:
                return False
    if 1 > month or month > 12:
        return False
    if MIN_YEAR > year or year > MAX_YEAR:
        return False
    return True


def is_leap_year(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
