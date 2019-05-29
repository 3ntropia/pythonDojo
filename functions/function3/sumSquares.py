# Para un numero entero N menor de 100 recibido como parametro, escribir un programa
# que utilice una funcion para devolver la suma de los cuadrados de aquellos
# numeros entre 1 y N que estan separados entre si por cuatro unidades. (1^2 + 5^2 +
# 9^2 + 13^2 + …)


def sum_minor_n(number):
    sum = 1
    count = 1
    while sum < number:
        count += 4
        if sum + count ** 2 < number:
            sum += count ** 2
        else:
            return sum
    return sum
