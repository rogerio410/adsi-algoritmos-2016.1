# Nao ta somando corretamente as fracoes.
# _*_ coding: utf-8 _*_

def main():
    n=input("Insira o N: ")
    denominador=1
    numerador=1
    for i in range(1,n+1):
        denominador*=i

    for i in range(n+1,1,-1):
        numerador+=(denominador/n)*1
    numerador*=1.0
    print "%d/%d" % (numerador*2,denominador)
    print "%.2f" % ((numerador*2)/denominador)



if __name__ == '__main__':
    main()