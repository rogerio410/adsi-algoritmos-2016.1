#coding: utf-8

def valida_numeros(a, b, c, d):
	if b>c and d>a and (c+d)>(a+b) and c>0 and d>0 and a%2==0:
		print("Valores Aceitos!")
	else:
		print("Valores Não Aceitos!")


def main():
	valor_a = int(input("Digite um Valor para A: "))
	valor_b = int(input("Digite um Valor para B: "))
	valor_c = int(input("Digite um Valor para C: "))
	valor_d = int(input("Digite um Valor para D: "))
	valida_numeros(valor_a, valor_b, valor_c, valor_d)



if __name__ == "__main__":
	main()
