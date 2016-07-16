# -*- coding: utf-8 -*-
"""
24.  A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos.
Escreva um algoritmo que leia o salário e o número de filhos de  N habitantes e escreva:  a) média de salário da população;
 ) média de número de filhos;  c) percentual de pessoas com salário de até R$ 1.000,00.
"""
def main ():
    print 'Senso população!'
    quantidade = input('Informe a quantidade de habitantes: ')
    soma_salario = 0.0
    soma_filhos = 0
    quantidade_pessoas_mil = 0

    for i in range(quantidade):
        salario = input('Salário: ')
        qt_filhos = input('Quantidade de filhos: ')
        soma_salario = soma_salario + salario
        soma_filhos = soma_filhos + qt_filhos
        if salario <= 1000:
            quantidade_pessoas_mil = quantidade_pessoas_mil + 1

    print 'A média de salário da população é: %.2f' % (soma_salario/ float(quantidade))
    print 'A média de números de filhos da população é: %.2f' % (soma_filhos/ float(quantidade))
    print 'O percentual de pessoas com salário de até R$10000,00 é: %.2f%%' % (quantidade_pessoas_mil/ float(quantidade)*100)

if __name__ == '__main__':
    main()