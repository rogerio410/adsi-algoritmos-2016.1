#__*__  encoding:utf8 __*__

def notas(nota_a,nota_b):
	media = (nota_a + nota_b) / 2.0

	if media >= 7 and media < 10:
		return "Aprovado"
	elif media < 7:
		return "Reprovado"
	elif media == 10:
		return "Aprovado com Distinção"

def main():
	nota_a = input("Digite a primeira nota: ")
	nota_b = input("Digite a segunda nota: ")
	resultado = notas(nota_a,nota_b)
	print resultado


if __name__ == '__main__':
	main()