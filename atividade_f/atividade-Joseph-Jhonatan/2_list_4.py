'''Leia 2 (duas)  notas parciais de um aluno, 
calcule a média e escreva a mensagem: o "Aprovado", se a média alcançada for maior ou igual a sete;
 o "Reprovado", se a média for menor do que sete; o "Aprovado com Distinção", se a média for igual a dez.'''

def main():
	nota_1 = float(input('Digite a 1° nota: '))
	nota_2 = float(input('Digite a 2° nota: '))
	media = (nota_1 + nota_2) / 2

	if(media==10):
		print('Aprovado com distinção.')
	elif(media >= 7):
		print('aprovado.')
	else:
		print('Reprovado.')

if __name__ == '__main__':
	main()