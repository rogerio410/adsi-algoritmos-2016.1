def calcula_salario(nome,salario,vendas):
	salario_final = (vendas * 0.15) + salario
	print 'O salario total de',nome,' sera de R$ %.2f' %salario_final
def main():	
		nome = raw_input('Qual o nome do vendedor?: ')
		salario = input('Qual o valor do salario?: ')
		vendas = input('Qual o valor das vendas efetuadas?: ')
		calcula_salario(nome,salario,vendas)
if __name__ == '__main__':
	main()
	
