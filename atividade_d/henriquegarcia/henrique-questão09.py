# _*_coding:utf-8_*_
#Questão 09

def multiplos(num):
    if num == 0:
        print("Não possui múltiplos")
    elif num != 0:
        multiplos = num * (num+1)
        print (multiplos)

def main():
    num = int(input("Informe um número inteiro: "))
    multiplos(num)
    print(multiplos(num))


if __name__ == '__main__':
    main()