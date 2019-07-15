"""Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas() Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >

GrabarPromedio() Graba en un archivo los promedios de las alturas de los atle-
tas presentes en el archivo generado en el paso anterior. La disciplina y el prome-
dio deben grabarse en líneas diferentes. Ejemplo:

<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo."""


def read_file(path):
    f = open(path, "r+")
    lines = f.readlines()
    f.close()
    return lines


def GrabarRangoAlturas(path):
    f = open(path, "w+")
    option = input("1- Cargar Deporte y Altura\n2- C para Cancelar")
    lines = []
    while option != 'C':
        lines.append(option + "\n")
        option = input("Siguiente: ")
    f.writelines(lines)
    f.close()


def GrabarPromedio(pathProm, path):
    lines = read_file(path)
    new_lines = []
    avg = -1
    counter = 1
    f = open(pathProm, "w+")
    for line in lines:
        if not line[:-1].isalpha():
            avg += float(line[:-1])
            counter += 1
        else:
            #Si es la primera
            if avg == -1:
                f.write(line)
            else:
                f.write(str(avg / counter) + "\n")
                f.write(line)
                avg = 0
                counter = 1
    #Ultima vez
    f.write(str(avg / counter) + "\n")
    f.close()


def MostrarMasAltos(path):
    f = open(path, "r+")
    l = f.readlines()
    print(l)
    f.close()


if __name__ == '__main__':
    GrabarRangoAlturas("alturas.txt")
    GrabarPromedio("promedios.txt", "alturas.txt")
