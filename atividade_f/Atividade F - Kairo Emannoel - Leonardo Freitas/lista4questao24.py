#_*_ coding:utf-8 _*_
def aritmetica(a0,r,limite):
    print "%d + %d = %d" % (a0,r,a0+r)
    for i in range(limite-1):
        a0+=r
        print "%d + %d = %d" % (a0, r, a0 + r)
def main():
    a0=input("Insira a0: ")
    r=input("Insira o R: ")
    limite=input("Insira o N: ")
    aritmetica(a0,r,limite)

if __name__ == '__main__':
    main()