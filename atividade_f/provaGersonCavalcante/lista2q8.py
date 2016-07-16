def main():
	valor_hora = input('Digite o valor hora: ')
	horas_trabalhadas = input('Diga a quantidade de horas trabalhadas: ')
	descontos(valor_hora,horas_trabalhadas)
def descontos(valor_hora, horas_trabalhadas):
	salario_bruto = valor_hora * horas_trabalhadas
	inss = (salario_bruto * 0.1)
	fgts = salario_bruto * 0.11
	if salario_bruto <= 900.00:
		salario_final = salario_bruto - inss
		total_descontos = inss

	elif salario_bruto > 900.00 and  salario_bruto <= 1500.00:
		salario_final = salario_bruto - inss
		ir = salario_bruto * 0.05
		salario_final -= ir
		total_descontos = inss + ir

	elif salario_bruto > 1500.00 and salario_bruto <=  2500.00:
		salario_final = salario_bruto - inss
		ir = salario_bruto * 0.1
		salario_final -= ir
		total_descontos = ir + inss
	else:
		salario_final = salario_bruto - inss
		ir = salario_bruto * 0.2
		salario_final -= ir
		total_descontos = inss + ir
	
	print 'Salario bruto = %d * %d\t : R$ %.2f' % (valor_hora,horas_trabalhadas,salario_bruto)
	print '(-)IR\t R$%.2f' % (ir)
	print '(-)INSS(10%%)\t : R$%f' % (inss)
	print 'FGTS(11%%)\t : R$%.2f' %(fgts)
	print 'Total de descontos\t : R$%.2f' %(total_descontos)
	print 'Salario Liquido\t : R$%.2f' %(salario_final)
if __name__ == '__main__':
	main()