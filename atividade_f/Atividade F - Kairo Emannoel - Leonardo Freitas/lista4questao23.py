#_*_ coding:utf-8 _*_
def progressao(a0,limite,constante):
    potencia = 0
    x=0
    for i in range(limite):
        print a0*(constante**potencia),
        potencia+=1
    #t1*r^n-1


def main():
    a0=input("Insira valor de a0: ")
    constante = input("Insira valor de R: ")
    limite=input("Insira limite da N: ")
    progressao(a0,limite,constante)

if __name__ == '__main__':
    main()