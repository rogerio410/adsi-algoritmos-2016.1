# -*- coding: utf-8 -*-
"""
15. Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária.
"""

def main():
    print 'Questão 15:'
    numero_decimal = input('Digite um numero (entre 0 e 255): ')
    expoente_2 = valor_expoente_2_aprox(numero_decimal)
    numero_binario = ''
    soma_binario = 0
    print 'exp ',expoente_2
    for i in range(expoente_2, -1, -1):
        print i
        valor_b = 2 ** i
        soma_binario = soma_binario + valor_b
        if soma_binario > numero_decimal:
            soma_binario = soma_binario - valor_b
            numero_binario += '0'
        else:
            numero_binario += '1'

    print numero_binario


def valor_expoente_2_aprox(numero_decimal):
    contador = 1
    numero = 1
    while numero < numero_decimal:
        numero = 2 ** (contador - 1)
        contador += 1
    return contador - 1



if __name__ == '__main__':
    main()
