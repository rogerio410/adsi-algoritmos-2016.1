def main():
   	nome_vend = raw_input('Digite o nome do vendedor:')
	salario_vend = float(input('Digite o salario fixo do vendedor:'))
	total_vend = float(input('Digite o total de vendas efetuadas pelo vendedor:'))
	comissao = total_vend * 0.15
	salario_total = salario_vend + comissao
	print('TOTAL = %.2f') %salario_total






if __name__ == '__main__':
	main()
