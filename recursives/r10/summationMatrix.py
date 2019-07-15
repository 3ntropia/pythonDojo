"""Escribir una función que sume todos los elementos de una matriz de M x N y de-
vuelva el resultado."""


def summation_recursive(m, i=0, j=0, s=0):
    if i == len(m) - 1 and j == len(m[i]) - 1:
        return s
    elif j == len(m[i]) - 1:
        return summation_recursive(m, i + 1, 0, s)
    else:
        return summation_recursive(m, i, j + 1, s + m[i][j])


if __name__ == '__main__':
    matrix = []
    row1 = [1, 2, 3, 4]
    row2 = [7, 8, 9, 10]
    row3 = [15, 16, 17, 18]
    matrix.append(row1)
    matrix.append(row2)
    matrix.append(row3)
    print(summation_recursive(matrix))
