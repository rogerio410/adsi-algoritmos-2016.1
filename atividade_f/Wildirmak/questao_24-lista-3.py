# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:10:01 2016

A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.

@author: wildrimak
"""

def main():
    quantidade_de_habitantes = input("Habitantes: ")
    soma_salario = 0
    media_salario = 0
    soma_filhos = 0
    media_numero_de_filhos = 0
    quantidade_de_salario_abaixo_de_mil = 0
    percentual_salario_ate_mil = 0
    
    for valor in range(1, quantidade_de_habitantes + 1):
        
        salario, numero_de_filhos = input("Qual o seu salario: "), input("Qual a quantidade de filhos: ")
        soma_salario = soma_salario + salario
        soma_filhos = soma_filhos + numero_de_filhos
        
        if salario <= 1000:
            quantidade_de_salario_abaixo_de_mil = quantidade_de_salario_abaixo_de_mil + 1
    
    media_salario = soma_salario/float(quantidade_de_habitantes)
    media_numero_de_filhos = soma_filhos/float(quantidade_de_habitantes)
    percentual_salario_ate_mil =  (100 * quantidade_de_salario_abaixo_de_mil)/float(quantidade_de_habitantes)
    
    print "A media do salario da população é: %g" %media_salario
    print "A media de numeros de filhos é: %g" %media_numero_de_filhos
    print "O percentual de pessoas com salario de até 1000R$ é: %g%%" %percentual_salario_ate_mil
if __name__ == "__main__":
    main()
