def main():
	numero_habitantes = input('Digite o numero de habitantes: ')

	total_salario = 0
	quantidade_filhos = 0
	quantidade_pessoas_salario_1000 = 0
	quantidade_habitantes = 0


	for i in range(1,numero_habitantes+1):

		salario = input('Digite o salario: ')
		numero_filhos = input('Digite o numero de filhos: ')

		total_salario = total_salario + salario
		quantidade_filhos = quantidade_filhos + numero_filhos
		quantidade_habitantes = quantidade_habitantes + 1

		if(salario <= 1000):
			quantidade_pessoas_salario_1000 = quantidade_pessoas_salario_1000 + 1

	media_salario = total_salario / float(quantidade_habitantes)
	media_filhos = quantidade_filhos / float(quantidade_habitantes)
	percentual_pessoas_salario_1000 = (quantidade_pessoas_salario_1000 * 100) / float(quantidade_habitantes)

	print('\nA media dos salarios dos habitantes eh %.2f ') % media_salario
	print('\nA media do numero de filhos eh %.1f ') % media_filhos
	print('\nO percentual de pessoas com salario ate 1.000,00 eh %.2f %% ') % percentual_pessoas_salario_1000




if __name__ == '__main__':
	main()