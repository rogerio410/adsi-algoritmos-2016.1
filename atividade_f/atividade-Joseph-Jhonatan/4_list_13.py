def main():
	soma_salario,soma_novo = 0,0
	while True:
		salario = float(input('Digite o salario: '))
		if(salario <=0):
			print('FIM.')
			break
		if(salario < 3000):
			salario_novo = salario * 1.25
		elif((salario >= 3000) and (salario < 6000)):
			salario_novo = salario * 1.2
		elif((salario >= 6000) and (salario < 10000)):
			salario_novo = salario * 1.15
		else:
			salario_novo = salario * 1.1
		print('Seu novo salario: R$ %.2f.'%salario_novo)
		soma_salario += salario
		soma_novo += salario_novo
	diferenca = soma_novo - soma_salario
	print('Soma salarios atuais: %.2f.'%soma_salario)
	print('Soma salarios reajustados: %.2f.'%soma_novo)
	print('Diferença da soma: %.2f.'%diferenca)

if __name__ == '__main__':
	main()