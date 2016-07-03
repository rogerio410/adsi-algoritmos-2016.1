## Mariano Barbosa de Carvalho Neto
def verificacao(a,b,c,d):
	if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
		return "valores aceitos"
	else: 
		return "Valores nao aceitos"

def main():
	a = input("Digite um numero inteiro: ")
	b = input("Digite um numero inteiro: ")
	c = input("Digite um numero inteiro: ")
	d = input("Digite um numero inteiro: ")
	verificacao(a,b,c,d)
	verificar = verificacao(a,b,c,d)
	print verificar

main()


