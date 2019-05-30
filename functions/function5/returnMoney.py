# Un comercio de electrodomesticos necesita para su linea de cajas un programa que
# le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
# dos numeros enteros, correspondientes al total de la compra y al dinero recibido.
# Informar cuantos billetes de cada denominacion deben ser entregados al cliente
# como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que
# existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error
# si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona
# con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
# de $20, 1 billete de $10 y 3 billetes de $1.

_FIVE_HUNDRED = 500
_ONE_HUNDRED = 100
_FIFTY = 50
_TWENTY = 20
_TEN = 10
_FIVE = 5


def return_money(total, money_given):
    if total > money_given:
        return "Dinero recibido insuficiente"
    elif total == money_given:
        return "No hay vuelto"
    else:
        bucket = ""
        money_to_be_return = money_given - total
        if money_to_be_return / _FIVE_HUNDRED >= 1:
            bucket = "$500 x" + str(money_to_be_return / _FIVE_HUNDRED) + " "
            money_to_be_return -= money_to_be_return / _FIVE_HUNDRED * _FIVE_HUNDRED
        if money_to_be_return / _ONE_HUNDRED >= 1:
            bucket += "$100 x" + str(money_to_be_return / _ONE_HUNDRED) + " "
            money_to_be_return -= money_to_be_return / _ONE_HUNDRED * _ONE_HUNDRED
        if money_to_be_return / _FIFTY >= 1:
            bucket += "$50 x" + str(money_to_be_return / _FIFTY) + " "
            money_to_be_return -= money_to_be_return / _FIFTY * _FIFTY
        if money_to_be_return / _TWENTY >= 1:
            bucket += "$20 x" + str(money_to_be_return / _TWENTY) + " "
            money_to_be_return -= money_to_be_return / _TWENTY * _TWENTY
        if money_to_be_return / _TEN >= 1:
            bucket += "$10 x" + str(money_to_be_return / _TEN) + " "
            money_to_be_return -= money_to_be_return / _TEN * _TEN
        if money_to_be_return / _FIVE >= 1:
            bucket += "$5 x" + str(money_to_be_return / _FIVE) + " "
            money_to_be_return -= money_to_be_return / _FIVE * _FIVE
        if money_to_be_return > 0:
            bucket += "$1 x" + str(money_to_be_return)
    return bucket
