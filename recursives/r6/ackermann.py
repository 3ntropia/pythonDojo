"""La función de Ackermann A(m,n) se define de la siguiente forma:
n+1 si m = 0
A(m-1,1) si n = 0
A(m-1,A(m,n-1)) de otro modo
Imprimir un cuadro con los valores que adopta la función para valores de m entre
0 y 3 y de n entre 0 y 7."""


def ackermann(m, n):
    print(m, n)
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


if __name__ == '__main__':
    ackermann(3, 3)
