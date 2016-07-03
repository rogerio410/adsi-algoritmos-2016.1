# -*- coding: utf-8 -*-

def tabulada_multiplicacao(numA, numB = 1):
	cont = 0
	if numB == 10:
		print numA * numB
	else:
		print numA * numB
		numB = numB + 1
		tabulada_multiplicacao(numA, numB)

def main():
	numA = input("Digite o primeiro numero a ser multiplicado: ")
	numB = input("Digite o segundo numero a ser multiplicado: ")
	tabulada_multiplicacao(numA, numB)

if __name__ == '__main__':
	main()
