# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 18:23:36 2016

@author: wildrimak
"""
def main():
    razao = input('Digite a razao da progressao: ')
    primeiro = input('Digite o primeiro termo da progressao: ')
    n = input('Digite o numero de termos da P.G: ')
    cont = 1
    while cont < n:
        print primeiro,
        primeiro = primeiro * razao
        cont += 1
    print primeiro
        
    
if __name__ == '__main__':
    main()