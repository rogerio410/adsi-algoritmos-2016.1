## Mariano Barbosa de Carvalho Neto
def verificar_se_triangulo(a,b,c):
	if (b - c) < a < (b + c) or (a - c) < b < (a + c) or (a - b) < c < (a + b):
		perimetro = a + b + c
		return ("Os valores digitados formam um triangulo de Perimetro = %.1f")%(perimetro)
	else:
		area = ((a +b)*c)/2
		return ("Os valores digitados nao formam um triangulo e sim um trapezio de Area = %.1f")%(area)

def main():
	a = input("Digite um valor: ")
	b = input("Digite um valor: ")
	c = input("Digite um valor: ")
	verificar_se_triangulo(a,b,c)
	verificacao = verificar_se_triangulo(a,b,c)
	print verificacao
main()
	    
