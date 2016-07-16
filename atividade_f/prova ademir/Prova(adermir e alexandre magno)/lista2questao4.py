def main ():
	nota1 = float(input('Digite a primeira nota:'))
	nota2 = float(input('Digite a segunda nota:'))
	media = (nota1 + nota2) / 2 
	if media > 7.0 and media < 10:
		print 'Aprovado'
	if media < 7.0 and media:
		print 'Reprovado'
	if media == 10.0:
	 	print 'Aprovado com Distincao'


if __name__ == '__main__':
	main()