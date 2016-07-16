def pesquisa():
    numero_de_habitantes = int(input("Insira o número de habitantes da cidade: "))
    contador = 0
    salario_total = 0
    num_total_filhos = 0
    ate_mil = 0
    while contador < numero_de_habitantes:
        numero_de_filhos = int(input("Insira o número de filhos que você tem: "))
        salario_bruto = float(input("Insira o valor do seu salário bruto, em R$: "))
        contador += 1
        salario_total += salario_bruto
        num_total_filhos += numero_de_filhos
        media_salario = (salario_total / numero_de_habitantes)
        media_filhos = (num_total_filhos / numero_de_habitantes)
        if salario_bruto <= 1000:
            ate_mil += 1
            percentual_mil = (ate_mil / numero_de_habitantes)
    print("A média de salario da populacão é R$ %.2f"% media_salario)
    print("A média de filhos da populacão é %d" %media_filhos)
    print("O percentual de pessoas com salários de até R$ 1000,00 é %.2f%%" %(percentual_mil*100))

if __name__ == '__main__':
    pesquisa()