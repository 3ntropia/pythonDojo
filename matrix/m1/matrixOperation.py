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


def replace_column(m, c, column):
    for i in range(len(column)):
        row = m[i]
        del row[c]
        row.insert(c, column[i])
    return m


def sort_row(m, r):
    return sorted(m[r])


def sort_whole_matrix_row(m):
    m_sort = []
    for j in range(len(m)):
        m_sort.append(sort_row(m, j))
    return m_sort


def order_column(m, c):
    column = get_column(m, c)
    column.sort()
    return replace_column(m, c, column)


def change_row(m, r1, r2):
    row1 = m[r1].copy()
    row2 = m[r2].copy()
    del m[r1]
    m.insert(r1, row2)
    del m[r2]
    m.insert(r2, row1)
    return m


def change_column(m, c1, c2):
    column1 = get_column(m, c1)
    column2 = get_column(m, c2)
    replace_column(m, c1, column2)
    replace_column(m, c2, column1)
    return m


def change_row_to_column(m, r, c):
    row = m[r]
    replace_column(m, c, row.copy())
    return m


def transpose_matrix(m):
    m_transpose = []
    for i in range(len(m)):
        m_transpose.append(get_column(m, i))
    return m_transpose


def is_regular(m):
    for j in m:
        if len(j) != len(m):
            return False
    return True


def is_simetric(m):
    m_copy = m.copy()
    if is_regular(m):
        return m_copy == transpose_matrix(m)
    return False


def inversed_transpose_matrix(m):
    m_transpose = []
    for i in range(len(m)):
        reversed_row = get_column(m, i)[::-1]
        m_transpose.insert(0, reversed_row)
    return m_transpose


def is_secundary_simetric(m):
    m_copy = m.copy()
    if is_regular(m):
        return m_copy == inversed_transpose_matrix(m)
    return False


def row_prom(m, r):
    int_sum = 0
    for j in m[r]:
        int_sum += j
    return int_sum / len(m[r])

#TODO
# Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
# Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas.


if __name__ == "__main__":
    ma = load_numbers(3)
    print(ma)
