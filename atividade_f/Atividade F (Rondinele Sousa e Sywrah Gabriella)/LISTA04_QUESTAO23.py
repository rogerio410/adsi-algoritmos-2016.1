# -*- coding: utf-8 -*-
"""
23. Escreva um algoritmo que leia a razão de uma PG (Progressão Geométrica) e o seu primeiro termo e escreva os N
termos da PG.  Ler o valor de N
"""
print('Questão 23:')
def main ():
    primeiro_termo = input('Digite o primeiro termo da PG: ')
    razao = input ('Digite a razão da PG: ')
    limite = input('Digite o limite da PG: ')
    pg(primeiro_termo, razao, limite)


def pg (a, razao, limite):
    print a,' ',
    for i in range (limite - 1):
        ax = a * razao
        a = ax
        print '%d ' % ax,



if __name__ == '__main__':
    main()