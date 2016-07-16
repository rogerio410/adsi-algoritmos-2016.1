#_*_ coding:utf-8 _*_
def binario(numero_decimal):
    numero_binario=""

    while numero_decimal>0.0:
        numero_binario+=str(numero_decimal%2)
        numero_decimal=numero_decimal/2

    print numero_binario[::-1]   #Slice? Ok.

def main():
    decimal=input("Insira numero em Decimal à ser convertido: ")
    binario(decimal)

if __name__ == '__main__':
    main()