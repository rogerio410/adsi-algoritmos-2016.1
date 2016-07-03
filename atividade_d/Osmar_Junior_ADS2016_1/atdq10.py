#coding: utf-8

def escreva_tabuada(numero, indice):
	if indice>10:
		print("Tabuada Feita!")
	else:
		print(">> ",numero,"x",indice," = ",(numero*indice))
		escreva_tabuada(numero, indice+1)

def main():
	numero = int(input("Digite um numero: "))
	indice = int(input("Digite um indice da tabuada (1-10): "))
	escreva_tabuada(numero, indice)


if __name__ == "__main__":
	main()
