# Escribir una funcion que reciba como parametro numero del 1 al 9 y devuelva el
# resultado de sumar n + nn + nnn + nnnn, donde n corresponde al numero recibido.
# Por ejemplo, si se ingresa 3 debe devolver 3702 (3+33+333+3333). Escribir
# tambien un programa para verificar el comportamiento de la funcion. No se
# permite utilizar facilidades de Python no vistas en clase.


def strange_sum(n):
    if 0 < n < 10:
        return n + int(str(n)*2) + int(str(n)*3) + int(str(n)*4)
    return -1
