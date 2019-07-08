"""Todo programa Python es susceptible de ser interrumpido mediante la pulsacion de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Reali-
zar un programa para imprimir los números enteros entre 1 y 100000, y que solici-
te confirmación al usuario antes de detenerse cuando se presione Ctrl-C."""


def print_number():
    counter = 0
    try:
        for counter in range(1000000):
            print(counter)
    except KeyboardInterrupt:
        continous = input("Do you want to stop? [Y/N]: ")
        if not continous:
            for last in range(counter, 100000):
                print(last)


if __name__ == '__main__':
    print_number()
