# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 23:13:17 2016

Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e
ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.

exemplo: ponto 1 (1, 3); ponto 2 (3, 4) -> distancia = raiz de 5

@author: wildrimak
"""



def main():

    import math
    x1, y1 = input("Informe a coordenada X do ponto 1: "), input("Informe a coordenada Y do ponto 1: ")
    x2, y2 = input("Informe a coordenada X do ponto 2: "), input("Informe a coordenada Y do ponto 2: ")
    distancia = math.sqrt(((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)))
    print "A distancia entre os dois pontos é: %g" %distancia

if __name__ == "__main__":
    main()