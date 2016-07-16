# -*- coding:utf-8 -*-
#Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária
def main():
	numero = int(input('Ínsira um numero de 0 á 255: '))
	
	segundo = numero % 2
	terceiro = int((numero / 2) % 2)
	quarto = int((numero / 4) % 2)
	quinto = int((numero / 8) % 2)
	sexto = int((numero / 16) % 2)
	setimo = int((numero / 32) % 2)
	oitavo = int((numero / 64) % 2)
	primeiro = int((numero / 128) % 2)

	binario =  segundo, terceiro, quarto, quinto, sexto, setimo, oitavo, primeiro
    
	print (binario)
	print ("inverter")
if __name__ == '__main__':
	main()