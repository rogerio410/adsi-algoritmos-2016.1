# Errada.. com só um salario de 1000 fica errada.
def main():
	salario_atual = 1
	salario_reajustado = 0
	soma_salario_atual = 0
	soma_salario_reajustado = 0

	while salario_atual != 0:
		salario_atual = input("DIGITE O SALARIO: ")
		if salario_atual> 0 and salario_atual <= 2999.99:
			salario_reajustado = salario_atual * 1.25
			print 'O SALARIO REAJUSTADO EH: ',salario_reajustado

		elif salario_atual >= 3000.00 and salario_atual <= 5999.99:
			salario_reajustado = salario_atual * 1.2
			print 'O SALARIO REAJUSTADO EH: ',salario_reajustado

		elif salario_atual >= 6000.00 and salario_atual <= 9999.99:
			salario_reajustado = salario_atual * 1.15
			print 'O SALARIO REAJUSTADO EH: ',salario_reajustado

		elif salario_atual >= 10000.00:
			salario_reajustado = salario_atual * 1.1
			print 'O SALARIO REAJUSTADO EH: ',salario_reajustado

		soma_salario_atual = soma_salario_atual + salario_atual
		soma_salario_reajustado = soma_salario_reajustado + salario_reajustado
		diferenca = soma_salario_reajustado - soma_salario_atual

	print 'A SOMA DOS SALARIOS ATUAIS E: ',soma_salario_atual
	print 'A SOMA DOS SALARIOS REAJUSTADOS E: ',soma_salario_reajustado
	print 'A DIFERENCA DAS SOMAS DOS SALARIOS E:',diferenca
		
		
		

if __name__ == '__main__':
	main()