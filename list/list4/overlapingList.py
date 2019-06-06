"""Definir una función superposición() que reciba como parámetros dos listas de cualquier tipo y devuelva True si
 tienen al menos un elemento en común, o False en caso contrario. Desarrollar un programa para
  verificar su comportamiento."""


def is_overlap(array_list, array_list2):
    for x in range(len(array_list)):
        if array_list2.count(array_list[x]) > 0:
            return True
    return False


def is_overlap_naive(array_list, array_list2):
    for x in range(len(array_list)):
        for y in range(len(array_list2)):
            if array_list2[y] == array_list[x]:
                return True
    return False


# Al ordenarse deberia encontrar iguales mas rapido.
def is_overlap_with_sort(array_list, array_list2):
    return is_overlap_naive(array_list.sort(), array_list2.sort())
