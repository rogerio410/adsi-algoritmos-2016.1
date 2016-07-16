
# Nao executa. Com erros nos IFs.

def main():

    sal = 0
    novo_salario = 0
    flag = 1

    while flag != "0":
        sal = float(input("Digite o salario "))

        if sal > 0 and < 2.999:

            novo_salario = sal * 1.25
        elif sal >= 3000 and <= 5999:
            novo_salario = sal * 1.20
        elif sal >= 6000 and <= 9999:
            novo_salario = sal * 1.15
        elif sal > 10.000:
            novo_salario = sal * 1.10

        soma += sal
        soma_sal += novo_salario
        print novo_salario
    print ("Reajustado %.2f"%soma_sal)
    print ("Atual %.2f"%soma)
    print ("Diferenca %.2f"%soma_sal-soma)

if __name__ == '__main__':
    main()
