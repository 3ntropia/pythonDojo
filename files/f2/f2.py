"""Escribir un programa que permita grabar un archivo los datos de lluvia caída du-
rante un año. Cada línea del archivo se grabará con el siguiente formato:
<dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
Los datos se generarán mediante números al azar, asegurándose que las fechas
sean válidas. La cantidad de registros también será un número al azar entre 50 y
200. Por último se solicita leer el archivo generado e imprimir un informe en for-
mato matricial donde cada columna represente a un mes y cada fila corresponda a
los días del mes. Imprimir además el total de lluvia caída en todo el año."""

from random import randint


def generate_list():
    data = []
    size = randint(50, 200)
    for index in range(size):
        day = randint(1, 30)
        month = randint(1, 12)
        rain = randint(100, 1000)
        line = str(day) + ";" + str(month) + ";" + str(rain) + "\n"
        data.append(line)
    return data


def generate_file(data, path):
    f = open(path, 'w+')
    for line in data:
        f.writelines(line)
    f.close()


def generate_empty_matrix():
    matrix = []
    for line in range(31):
        row = [0 for _ in range(12)]
        matrix.append(row)
    return matrix


def add_to_matrix(matrix, split_line):
    row = matrix[int(split_line[0]) - 1]
    row[int(split_line[1]) - 1] = int(split_line[2])


def read_file(path):
    f = open(path, 'r+')
    matrix = generate_empty_matrix()
    for line in f.readlines():
        split_line = line.split(";")
        add_to_matrix(matrix, split_line)
    f.close()
    return matrix


if __name__ == '__main__':
    __path = "rain.txt"

    data = generate_list()
    generate_file(data, __path)
    matrix = read_file(__path)
    #TODO falta sumar... recorriendo todas las filas
    for line in matrix:
        print(line)
