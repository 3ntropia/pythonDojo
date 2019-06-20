"""Los números de claves de dos cajas fuertes están intercalados dentro de un nú-
mero entero llamado "clave maestra", cuya longitud no se conoce. Realizar un pro-
grama para obtener ambas claves, donde la primera se construye con los dígitos
impares de la clave maestra y la segunda con los dígitos pares. Los dígitos se
numeran desde la izquierda. Ejemplo: Si clave maestra = 18293, la clave 1 sería
123 y la clave 2 sería 89."""


def get_keys(string):
    key = ""
    key2 = ""
    for i in range(len(string)):
        if i % 2 == 0:
            key += str(string[i])
        else:
            key2 += str(string[i])
    return key, key2
