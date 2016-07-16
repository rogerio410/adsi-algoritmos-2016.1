# -*- coding: utf-8 -*-
"""
42. Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2),
escreva a distância entre eles, conforme fórmula abaixo.
"""
import math
def main ():
    print 'Questão 42:'
    x1 = input('Digite o valor de X1:')
    y1 = input('Digite o valor de Y1:')
    x2 = input('Digite o valor de X2:')
    y2 = input('Digite o valor de Y2:')
    diferenca_quadrado_x = (x2 - x1) ** 2
    diferenca_quadrado_y = (y2 - y1) ** 2
    diferenca_pontos = math.sqrt(diferenca_quadrado_x + diferenca_quadrado_y)
    print 'A diferença entre os pontos é: ' , diferenca_pontos





if __name__ == '__main__':
    main()