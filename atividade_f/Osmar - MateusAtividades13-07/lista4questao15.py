# Error de Recursividade..
def main():
    valor = int(input("digite um valor entre 0 e 255:"))
    if valor < 0 or valor > 255:
        print("o valor precisa estar entre 0 e 255")
        main()
    binario(valor)
    #hex(valor)

def binario(num):
    count = num
    exp1 = 0
    exp2 = 0
    exp3 = 0
    exp4 = 0
    exp5 = 0
    exp6 = 0
    exp7 = 0
    exp8 = 0
    if num % 2 == 1:
        exp1 = 1
    num = num/2
    if num == 1:
        exp8 = 1
    binario(num)





if __name__=="__main__":
    main()