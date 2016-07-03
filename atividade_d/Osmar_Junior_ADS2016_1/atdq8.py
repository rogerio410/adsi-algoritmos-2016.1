#coding: utf-8

def valida_triangulo(a, b, c):
	if a>((b-c)*-1) and a<(b+c) and b>((a-c)*-1) and b<(a+c) and c>((a-b)*-1) and c<(a+b):
		resultado = a+b+c
		print("Perímetro: %.1f"%resultado,".")
	else:
		resultado = ((a+b)*c)/2
		print("Área: %.1f"%resultado,".")



def main():
	lado_a = int(input("Digite um Valor para o Lado A do Triângulo: "))
	lado_b = int(input("Digite um Valor para o Lado B do Triângulo: "))
	lado_c = int(input("Digite um Valor para o Lado C do Triângulo: "))
	valida_triangulo(lado_a, lado_b, lado_c)


if __name__ == "__main__":
	main()
