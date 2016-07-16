'''A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.'''

def main():
    habitantes = int(input('Informe o número de habitantes: '))
    cont_salario = 0.00
    cont_filhos = 0
    cont_situacao = 0
    for pesquisa in range(1, habitantes +1):
        numero_filhos = int(input('Informe a quantidade de filhos: '))
        cont_filhos += numero_filhos
        salario_habitante = float(input('Informe seu salário: '))
        cont_salario += salario_habitante
        if salario_habitante <= 1000.00:
            cont_situacao += 1
    media_salario = cont_salario/habitantes
    media_filhos = cont_filhos/habitantes
    percentual_situacao = (cont_situacao*100)/habitantes
    print('A média de salário da população é: %.2f' % media_salario)
    print('A média de  número de filhos da população é: %.2f' % media_filhos)
    print('O percentual de habitantes com salário de até R$1000.00 é: %.2f' % percentual_situacao)





if __name__ == '__main__':
    main()