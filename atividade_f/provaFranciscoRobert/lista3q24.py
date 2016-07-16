def main():
	numero_de_habitantes = input('Qual o numero de habitates: ')
	senso(numero_de_habitantes)
def senso(numero_de_habitantes):
	contador_salario = 0
	contador_filhos = 0
	contador_salario_ate_mil = 0
	percentual_salario_ate_mil = 0
	for contador in range(numero_de_habitantes,0,-1):
		salario = input('valor salario:' )
		numero_filhos = input('Quantidade de filhos: ')
		contador_salario += salario
		contador_filhos += numero_filhos
		if salario <= 1000.00:
			contador_salario_ate_mil += 1
	media_salario = contador_salario / numero_de_habitantes
	media_de_filhos = contador_filhos / numero_de_habitantes
	percentual_salario_ate_mil = (contador_salario_ate_mil * 100) / numero_de_habitantes
	print 'Media de salario da populacao: %.2f' %(media_salario)
	print 'Media de filhos: %d'%media_de_filhos
	print 'Porcentagem de pessoas com salario ate R$1000,00 = %.2f %%'%percentual_salario_ate_mil	

if __name__ == '__main__':
	main()