"""Realizar una función recursiva para imprimir una matriz de M x N."""


def print_recursive(matrix, i=0, j=0):
    if i < len(matrix):
        row = matrix[i]
        if i == len(matrix) and j == len(row):
            return
        elif j == len(row):
            print_recursive(matrix, i + 1)
        else:
            print(row[j])
            print_recursive(matrix, i, j + 1)


if __name__ == '__main__':
    matrix = []
    row1 = [1, 2, 3, 4]
    row2 = [7, 8, 9, 10]
    row3 = [15, 16, 17, 18]
    matrix.append(row1)
    matrix.append(row2)
    matrix.append(row3)
    print_recursive(matrix)
