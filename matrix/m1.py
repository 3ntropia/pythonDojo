"""Desarrollar cada una de las siguientes funciones y escribir un programa que permita
verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Intercambiar una fila por una columna, cuyos números se reciben como parámetro.
f. Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
g. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
h. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número
se recibe como parámetro.
i. Determinar si la matriz es simétrica con respecto a su diagonal principal.
j. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
k. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
NOTA: El valor de N debe establecerlo el programador o ingresarse por teclado,
pero las funciones deben servir aunque este valor se modifique."""
from list.list7 import sortList

def load_numbers(size):
    m = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(int(input("ingrese num para i=" + str(i) + " j=" + str(j) + " :")))
        m.append(row)
    return m


def get_column(m, c):
    return [row[c] for row in m]


def order_column(m, c, size):
    column = get_column(m, c)
    sortList.sort()




if __name__ == "__main__":
    m = load_numbers(3)
    print(m)
