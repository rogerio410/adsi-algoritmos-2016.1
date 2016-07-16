#_*_ coding: utf-8 _*_
def calculo(x1,y1,x2,y2):
    import math

    distancia=math.sqrt(((x2-x1)**2)+((y2-y1)**2))

    print "Distancia = %.4f" % (distancia)


def main():

    print "Ponto 1"
    x1 = float(input("Insira X1: "))
    y1 = float(input("Insira Y1: "))

    print "Ponto 2"
    x2 = float(input("Insira X2: "))
    y2 = float(input("Insira Y2: "))

    calculo(x1,y1,x2,y2)

if __name__ == '__main__':
    main()