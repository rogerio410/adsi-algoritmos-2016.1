def main():
	nota1, nota2 = input("Digite a primeira nota: "), input("Digite a segunda nota: ")
	media(nota1, nota2)

def media(nota1, nota2):
	media = ( nota1 + nota2 ) / 2
	if media >= 7 and media < 10:
		print "Aprovado"
	elif media < 7:
		print "Reprovado"
	elif media == 10:
		print "Aprovado com Distincao"


if __name__ == '__main__':
	main()