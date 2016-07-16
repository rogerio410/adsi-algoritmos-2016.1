# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:48:17 2016

Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
o "Aprovado", se a média alcançada for maior ou igual a sete;
o "Reprovado", se a média for menor do que sete;
o "Aprovado com Distinção", se a média for igual a dez.

@author: wildrimak
"""

def main():
    
    nota_1, nota_2 = input("Informe nota 1: "), input("Informe nota 2: ")
    media = (nota_1 + nota_2)/2.0
    
    if media == 10:
        print "Aprovado com Distinção"
    elif media >= 7 and media < 10:
        print "Aprovado"
    else:
        print "Reprovado"
    
    
if __name__ == "__main__":
    main()