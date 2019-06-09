"""2048 es un juego que se desarrolla en una cuadrícula de 4 x 4, donde en cada celda
hay una baldosa con un número 2 o 4 generados al azar. Se utilizan las teclas
de dirección para mover las baldosas: 4 (izquierda), 6 (derecha), 8 (arriba) y 2
(abajo). Estas baldosas se deslizan sobre el tablero en el sentido indicado por la
tecla presionada. Si dos baldosas con el mismo número "colisionan" durante un
movimiento, se combinarán en una nueva baldosa cuyo valor será la suma de los
valores de las dos baldosas originales, es decir que si dos baldosas con el número
4 colisionan, éstas se combinarán en una baldosa con el número 8. Sin embargo la
baldosa resultante no podrá combinarse con otra en esa misma jugada.
Las jugadas se realizan ingresando la fila y columna de la baldosa a desplazar y la
dirección en que se mueve. En el espacio vacío dejado por la baldosa desplazada
aparecerá una nueva baldosa conteniendo un número 2 o 4, generado al azar. El
juego finaliza cuando se obtiene una baldosa con el número 2048. Escribir un programa
que permita jugarlo e informe la cantidad de jugadas realizadas hasta finalizar."""


