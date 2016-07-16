# -*- coding: utf-8 -*-
"""4. Leia 2 (duas)  notas parciais de um aluno, calcule a média e escreva a mensagem: o "Aprovado",
se a média alcançada for maior ou igual a sete; o "Reprovado", se a média for menor do que sete; o
"Aprovado com Distinção", se a média for igual a dez.
"""

def main():
    print 'Questão 02:'
    nota1 = input('Digite a primeira nota: ')
    nota2 = input('Digite a primeira nota: ')
    media = (nota1 + nota2)/2.0
    if media == 10:
        print 'ALUNO APROVADO COM DISTINÇÂO!'
    elif media >= 7:
        print 'APROVADO!'
    else:
        print 'REPROVADO!'

if __name__ == '__main__':
    main()