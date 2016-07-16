# -*- coding: utf-8 -*-
"""
16. Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci (0,1,1,2,3,5,8,...).
O valor lido para N sempre será maior ou igual a 2.
"""
def main():
    print 'Questão 16:'
    n = int (input('Digite um número maior ou igual a 2: '))
    penultimo = 0
    ultimo = 1

    print penultimo, ultimo, fibonacci(penultimo, ultimo, 2, n)

def fibonacci(anterior, atual, contador, limite):
    if contador >= limite:
        return ''
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador = contador + 1
    lista = str(atual) + ' ' + fibonacci(anterior, atual, contador, limite)
    return lista


if __name__ == '__main__':
    main()