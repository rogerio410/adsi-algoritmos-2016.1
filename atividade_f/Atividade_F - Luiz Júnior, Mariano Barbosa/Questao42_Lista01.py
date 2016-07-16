
def Questao42_Lista01(x1, y1, x2, y2):

    distancia = (((x2-x1)**2) + ((y2-y1)**2)) ** 0.5
    
    print "A distancia entre os pontos X e Y foi igual a %.2f." % distancia

def main():

    x1 = input("Digite o valor do primeiro ponto do eixo x: ")
    y1 = input("Digite o valor do primeiro ponto do eixo y: ")
    x2 = input("Digite o valor do segundo ponto do eixo x: ")
    y2 = input("Digite o valor do segundo ponto do eixo y: ")

    Questao42_Lista01(x1, y1, x2, y2)

if __name__ == "__main__":

    main()
