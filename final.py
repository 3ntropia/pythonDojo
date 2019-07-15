"""Utilizar el Block de notas o el editor del Visual Studio para crear un archivo de texto cuyas líneas pueden tener indis-
tintamente cualquiera de los siguientes formatos:

Formato 1: Compra de mercaderías

DD MM AAAA DDDDDDDDDDDDDDDDDDDD NNN PPP.PP

Formato 2: Venta de mercaderías

DD MM AAAA NNN DDDDDDDDDDDDDDDDDDDD PPP.PP

Donde:
DD = Número de día, en dos posiciones. (01 a 31, comienza en columna 0)
MM = Número de mes, en dos posiciones. (01 a 12, comienza en columna 3)
AAAA = Número de año, en cuatro posiciones. (comienza en columna 6)
DDD... = Nombre del producto (20 posiciones, rellenado con espacios si la longitud es menor que 20. Comienza

en columna 11 o 16 según el tipo de registro)

NNN = Cantidad de unidades compradas o vendidas. (001 a 999, comienza en columna 32 u 11)
PPP.PP = Precio por unidad. Número real (tres dígitos y dos decimales, comienza en columna 36)
Ejemplo:
12 08 2009 035 RESMA PAPEL OBRA 70G 101.15 <– Venta de mercaderías
08 10 2009 TIJERA ESCOLAR PLAST 150 064.21 <– Compra de mercaderías
El mismo archivo contiene registros de ambos formatos intercalados sin ningún criterio particular.
Se solicita imprimir un listado con la cantidad en stock para cada producto, la que se obtiene sumando las compras y

restando las ventas de cada uno de ellos. El listado debe mostrarse ordenado en forma descendente según la canti-
dad en stock. Imprimir también el resultado del ejercicio para el año 2009, el que se obtiene restando el total obteni-
do por ventas menos el total invertido en compras, considerando solamente aquellas operaciones del año 2009.

No se conoce la cantidad de productos. Tampoco es posible estimar una cantidad para este valor."""
