"""Eliminar de una lista de palabras las palabras que se encuentren en una segunda
lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante."""


def remove_repeated(array_list, words_array):
    right_array = []
    for x in range(len(array_list)):
        add_to_list = True
        for y in range(len(words_array)):
            if words_array[y] == array_list[x]:
                add_to_list = False
                continue
        if add_to_list:
            right_array.append(array_list[x])
    return right_array
