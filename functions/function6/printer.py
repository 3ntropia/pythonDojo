# Escribir dos funciones para imprimir por pantalla cada uno de los siguientes
# patrones de asteriscos, donde la cantidad de filas se recibe como parametro:
# **********         **
# **********         ****
# **********         ******
# **********         ********
# **********         **********


def printer(lines):
    for x in range(0, lines):
        print('**********           ' + '**' * (x + 1))


if __name__ == '__main__':
    printer(3)
    printer(8)
