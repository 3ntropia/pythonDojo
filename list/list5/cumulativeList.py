"""Escribir un programa que calcule la suma acumulada a partir de una lista de números. El programa debe
 generar una nueva lista donde el primer elemento es el mismo de la lista original,
  el segundo elemento es la suma del primero más el segundo, el tercer elemento es la suma del primero
  más el segundo más el tercero y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1,3,6]."""


def sum_array_cumulative(array_list):
    array_sum = []
    sum_var = 0
    for x in range(len(array_list)):
        sum_var += array_list[x]
        array_sum.append(sum_var)
    return array_sum


