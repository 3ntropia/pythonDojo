"""Escribir un programa para crear una lista por comprensión con los naipes de la baraja
española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros",
"2 Oros"... ]. Imprimir la lista por pantalla."""


def create_cards(type):
    return [str(x) + " " + type for x in range(1, 13)]


def create_deck():
    oros = create_cards("Oros")
    copas = create_cards("Copas")
    bastos = create_cards("Bastos")
    espadas = create_cards("Espadas")
    deck = oros + copas + bastos + espadas
    return deck


if __name__ == '__main__':
    print(create_deck())
