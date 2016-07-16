


def main():
    continuar = 1
    soma_salarios, qtd_filhos = 0, 0
    contador_salario_mil = 0
    total_pessoas = 0
    while continuar == 1:
        salario = float(input("Digite o salario em R$: "))
        numero_filhos = int(input("Numero de filhos: "))
        soma_salarios = soma_salarios + salario
        qtd_filhos = qtd_filhos + numero_filhos
        total_pessoas = total_pessoas + 1
        if salario <= 1000.00:
            contador_salario_mil = contador_salario_mil + 1
        continuar = int(input("Continuar entrevista? 1 - SIM, 2 - NAO "))

    percentual = (contador_salario_mil / total_pessoas) * 100.0
    print("Media de salario dos entrevistados R$ %.2f"%(soma_salarios/float(total_pessoas)))
    print("Media da quantidade de filhos: %.2f"%(qtd_filhos/total_pessoas))
    print("Percentual de pessoas com salario ate R$ 1000.00: %.1f %%"% percentual)


if __name__ == "__main__":
    main()