import math

def distancia_entre_pontos(x1,y1,x2,y2):
    distancia = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    return distancia

def main():
    print(">> Distância entre dois pontos <<")
    x1 = int(input("Digite um Valor para X1: "))
    y1 = int(input("Digite um Valor para Y1: "))
    x2 = int(input("Digite um Valor para X2: "))
    y2 = int(input("Digite um Valor para Y2: "))
    distancia = distancia_entre_pontos(x1,y1,x2,y2)
    print("A distância obtida pela raíz de (x2-x1)²+(y2-y1)² é igual a %.2f"%distancia,".")

if __name__ == "__main__":
    main()
