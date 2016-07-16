# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:55:25 2016

@author: wildrimak
"""

def main():
    razao = input('digite a razao da progressao: ')
    primeiro = input('digite o primeiro termo da progressao: ')
    n = input('digite o numero de termos da P.A: ')
    cont = 1
    while cont < n:
        print primeiro,
        primeiro = primeiro+razao
        cont += 1
    print primeiro
        
    
if __name__ == '__main__':
    main()