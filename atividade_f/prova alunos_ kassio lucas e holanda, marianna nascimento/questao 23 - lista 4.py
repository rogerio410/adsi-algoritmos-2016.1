# -*- coding: utf-8 -*-


#Escreva um algoritmo que leia a razão de uma PG (Progressão Geométrica) e o seu primeiro termo e escreva os N termos da PG.  Ler o valor de N.

""" PAra imprimir N Termos ... e nao Limite <= N"""

primeiro  = input("escreva o primeiro termo: ")
razao = input("escreva a razao da PG: ")
n = input("escreva o numero para finalizar: ")

while n > primeiro:
    valor_i = primeiro
    print primeiro,
    primeiro = primeiro * razao


