# Nao fez recursivo.

#coding:utf-8

def main():
    numero = input("insira um valor de limite >2. tecle 's' para sair: ")
    if numero == "s":
        quit()
    numero = int(numero)
    if numero < 2:
        print (" o valor precisa ser maior que 2.")
        main()
    fibronacci(numero)

def fibronacci(n):
    count = 0
    a = 1
    b = 0
    while count < n:
        c = a+b
        a = b
        b = c
        print (c)
        count +=1
    main()


if __name__=="__main__":
    main()