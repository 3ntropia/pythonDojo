# Una persona desea llevar el control de los gastos realizados al viajar en el subterraneo
# dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema
# de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar
# una función que reciba como parametro la cantidad de viajes realizados en un
# determinado mes y devuelva el total gastado en viajes. Realizar tambien un programa
# para verificar el comportamiento de la funcion.
# Cantidad de viajes Valor del pasaje
# 1 a 20 Averiguar valor actualizado
# 21 a 30 20% de descuento sobre tarifa maxima
# 31 a 40 30% de descuento sobre tarifa maxima
# Más de 40 40% de descuento sobre tarifa maxima

_TRIP_PRICE = 20
_FIRST_STEP = 20
_SECOND_STEP = 30
_THIRD_STEP = 40


def spend_calculator(trips):
    if 0 < trips < 21:
        return trips * _TRIP_PRICE
    elif 21 < trips < 31:
        return _FIRST_STEP * _TRIP_PRICE + (trips - _FIRST_STEP) * _TRIP_PRICE
    elif 31 < trips < 41:
        return _SECOND_STEP * _TRIP_PRICE + (trips - _SECOND_STEP) * _TRIP_PRICE
    elif 41 < trips:
        return _SECOND_STEP * _TRIP_PRICE + (trips - _SECOND_STEP) * _TRIP_PRICE + _THIRD_STEP * _TRIP_PRICE
    else:
        return 0
