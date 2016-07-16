
def main():
	media_salario,soma_salario,cont,soma_filhos,media_filhos,cont_salario = 0,0,0,0,0,0
	print('Para sair digite o numero zero.')
	while True:
		salario = float(input('Digite o seu salario: '))
		if(salario <= 0):
			print('FIM.')
			break
		n_filhos = int(input('Digite o numero de filhos: '))
		cont += 1
		if(salario<=1000):
			cont_salario += 1
		soma_salario = soma_salario + salario
		soma_filhos = soma_filhos + n_filhos
	media_salario = soma_salario / cont	
	media_filhos = soma_filhos / cont
	porcen = (cont_salario / cont) * 100
	print('\nMedia de salarios: %.2f'%media_salario)
	print('\nMedia de filhos: %.2f'%media_filhos)
	print('\nPercentual de pessoas com um salario ate R$ 1000: %d %%.'%porcen)

if __name__ == '__main__':
	main()