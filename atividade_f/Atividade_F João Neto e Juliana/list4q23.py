# -*- coding: utf-8 -*-
# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica
# que tem por valor inicial A0 e razão R.

def progressao_geometrica(valor_inicial, limite, razao):
    valor_atual = valor_inicial
    for i in range(1, limite+1):
        print valor_atual
        valor_atual = valor_atual * razao
def main():
    valor_inicial = input("digite um valor inicial: ")
    limite = input("digite a quantidade N: ")
    razao = input("digite um valor para Razao: ")
    progressao_geometrica(valor_inicial, limite, razao)


if __name__ == "__main__":
    main()

