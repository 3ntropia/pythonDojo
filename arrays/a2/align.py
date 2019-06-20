"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas."""


def print_center(string):
    print('{:{align}{width}}'.format(string, align='^', width='80'))


if __name__ == '__main__':
    print_center("This is black magic!")
