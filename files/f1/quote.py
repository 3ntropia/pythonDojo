"""Desarrollar un programa para eliminar todos los comentarios de un programa es-
crito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o do-
bles) y que también se considera comentario a las cadenas de documentación
(docstrings)."""


def quote(path):
    file = open(path, "r+")
    with open(path, "r+") as f:
        lines = f.readlines()
        for line in lines:
            file.write("#" + line)
    file.close()


def unquote(path):
    lines = open(path, 'r').readlines()
    newlines = []
    for line in lines:
        newline = line.replace("#", "")
        newlines.append(newline)
    f = open(path, 'w')
    f.writelines(newlines)
    f.close()


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


if __name__ == '__main__':
    unquote("writable.py")
