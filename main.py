#1
def potencia(base=2, exponente=2):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print(potencia())

#2

def torres_de_hanoi(numero, origen, destino, auxiliar):
    if numero == 1:
        print(f"1er disco {origen} a {destino}")
    else:
        torres_de_hanoi(numero - 1, origen, auxiliar, destino)
        print(f"disco {numero} de {origen} a {destino}")
        torres_de_hanoi(numero - 1, auxiliar, destino, origen)

torres_de_hanoi(3, 'A', 'B', 'C')
