
from math import sqrt , pow


def quadrado_da_diferenca(valor_um,valor_dois):

    diferenca = pow(valor_um - valor_dois,2)

    return diferenca

def main():

    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    distancia = sqrt(quadrado_da_diferenca(x2,x1) + quadrado_da_diferenca(y2,y1))

    print("O valor da distancia eh %.4f"%distancia)




if __name__ == '__main__':
    main()
