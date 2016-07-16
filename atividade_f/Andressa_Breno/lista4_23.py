""" PAra imprimir N Termos ... e nao Limite <= N"""
# -*- coding: utf-8 -*-
def pg(a0, razao, n): #a - value q - factor n- number of elements

	while True:
		a0 *= razao
		if a0 <= n:
			print a0
		else:
			break
		

def main():
	a0 = input('Digite o valor inicial A0: ')
	n = input('Digite o n: ')
	razao = input('Digite a razao para a progressao geometrica: ')
	pg(a0, razao, n)

if __name__ == '__main__':
	main()
