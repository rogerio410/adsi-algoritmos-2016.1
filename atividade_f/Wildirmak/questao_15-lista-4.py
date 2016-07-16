# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 18:39:19 2016

15. Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária
e na base hexadecimal.

@author: wildrimak
"""

def main():
    numero_decimal = input("Informe um número entre 0 e 255: ")
    potencia_de_dois = 128.0
    primeiro, segundo, terceiro, quarto, quinto, sexto, setimo, oitavo = 0, 0, 0, 0, 0, 0, 0, 0
    if numero_decimal <= 0 or numero_decimal >= 255:
        print "Informe um numero entre 0 e 255"
    else:
        while True:
            if numero_decimal/potencia_de_dois == 1:
                primeiro = 1
                numero_decimal = numero_decimal%potencia_de_dois
                potencia_de_dois = potencia_de_dois/2
            
            if potencia_de_dois == 0.5:
                break
                
    
if __name__ == "__main__":
    main()