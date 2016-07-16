# -*- coding: utf-8 -*-
"""
Leia N, calcule e escreva o valor de S =
"""
def main():
    print 'Questão 17:'
    n = input('Digite um valor: ')
    soma = 0
    valor_mmc = 1
    denominador_anterior = 1
    soma_numeradores = 0
    for item in range(1, n +1):
        soma = soma + (1/float(item))
        denominador_anterior = valor_mmc
        valor_mmc = mmc(valor_mmc,item)
        soma_numeradores = valor_mmc /denominador_anterior * soma_numeradores + valor_mmc / item

    print 'A soma da sequência é: %.2f = %d/%d' %(soma, soma_numeradores, valor_mmc)


def mmc (numero1, numero2):
    contador = 1
    while contador%numero1 != 0 or contador%numero2 != 0:
        contador += 1
    return contador

if __name__ == '__main__':
    main()
