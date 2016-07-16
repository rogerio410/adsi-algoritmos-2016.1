# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:58:37 2016

@author: wildrimak
"""

def main():
    leia_n = input("Digite o valor de N: ")
    somatorio = 0
    
    for valor in range(1, leia_n + 1):
        somatorio = somatorio +  1/float(valor) 
        
    
    
    print somatorio
if __name__ == "__main__":
    main()
