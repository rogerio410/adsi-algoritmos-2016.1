from math import sqrt as raiz

def distancia_dois_pontos(x1, y1, x2, y2):
    distancia = raiz((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("A distância entre os dois pontos é %d" %distancia)

def main():
    print("Distância entre dois pontos")
    x1 = int(input("Insira x1: "))
    y1 = int(input("Insira y1: "))
    x2 = int(input("Insira x2: "))
    y2 = int(input("Insira y2: "))
    distancia_dois_pontos(x1, y1, x2, y2)

if __name__ == '__main__':
    main()