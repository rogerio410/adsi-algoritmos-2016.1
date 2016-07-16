# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 10:50:13 2016

16
->Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
(0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

OBS: o termo 0 da sequencia de fibonacci é 0
     o termo 1 da sequencia de fibonacci é 1
     o termo 2 da sequencia de fibonacci é 1
     o termo 3 da sequencia de fibonacci é 2
     
@author: wildrimak
"""

#Errada.

def questao_16(cont):
    leia_n = input("Informe N maior ou igual a 2: ")
    x = 0
    while cont <= leia_n:
            x = x + 1
            cont += 1
            print x
            questao_16(cont)
            
    
        

if __name__ == "__main__":
    cont = 1
    questao_16(cont)