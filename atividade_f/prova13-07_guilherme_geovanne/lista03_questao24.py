
def prefeitura():

    salario = 0
    numero_filhos = 0
    flag = 1
    media_populacao = 0
    media_numero_filhos = 0
    percentual_pessoas = 0
    soma_salario = 0
    soma_filho = 0
    cont = 0
    cont_mil = 0
    while flag != "0":
        salario = float(input("sal: "))
        numero_filhos = int(input("numero filhos: "))

        if salario <= 1000:
            cont_mil += 1

        cont += 1
        soma_filho += numero_filhos
        soma_salario += salario

        flag = input(("Quer continuar 1 para sim 0 para nao"))

    media_populacao = soma_salario/cont
    media_numero_filhos = soma_filho/cont
    percentual_pessoas = (cont_mil/cont) * 100

    print("Media da populacao %.2f"%media_populacao)
    print("Media do numero de filhos %.2f"%media_numero_filhos)
    print("Percentual de pessoas %.2f"%percentual_pessoas)

def main():
    prefeitura()

if __name__ == '__main__':
    main()
