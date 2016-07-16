def main():
	print 'Digite as notas entre 0 e 10:'
	nota_A = input('Digite a primeira nota:\n')
	nota_B = input('Digite a segunda nota:\n')
	notas(nota_A, nota_B)

def notas(nota_A, nota_B):
	media=(nota_A+nota_B)/2
	if media == 10:
		print 'Aprovado com distincao!'
	elif media < 7:
		print 'Reprovado!'
	else:
		print 'Aprovado'

if __name__ == '__main__':
	main()