# -*- coding: utf-8 -*-
"""
24. Escreva um algoritmo que leia a razão de uma PA (Progressão Aritmética) e o seu primeiro termo e escreva os N
termos da PA.  Ler o valor de N.
"""
print('Questão 24:')
def main ():
    primeiro_termo = input('Digite o primeiro termo da PA: ')
    razao = input ('Digite a razão da PA: ')
    limite = input('Digite o limite da PA: ')
    pa(primeiro_termo, razao, limite)


def pa (a, razao, limite):
   print a,' ',
   for i in range (limite - 1):
        ax = a + razao
        a = ax
        print '%d ' % ax,



if __name__ == '__main__':
    main()