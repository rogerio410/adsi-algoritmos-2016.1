# -*- coding: utf-8 -*-
valorA = input('Digite o primeiro valor inteiro: ')
valorB = input('Digite o segundo valor inteiro: ')
valorC = input('Digite o terceiro valor inteiro: ')
valorD = input('Digite o quarto valor inteiro: ')

somaAB = valorA + valorB
somaCD = valorC + valorD

if valorB > valorC and valorD > valorA and somaCD > somaAB and valorC > 0 and valorD > 0 and valorA%2 == 0:
    print 'Valores não aceitos!!!'
else:
    print 'Valores aceitos!!'