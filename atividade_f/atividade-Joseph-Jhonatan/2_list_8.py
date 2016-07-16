def main():
	horas_trabalhadas = int(input('Digite o numero de horas trabalhadas por dia do trabalhador: '))
	valor_hora = float(input('Digite quanto vale a hora trabalhada: '))
	salario_bruto =  horas_trabalhadas * valor_hora
	fgts = salario_bruto * 0.11
	sindic = salario_bruto * 0.03
	ir = 0
	if(salario_bruto > 900):
		if(salario_bruto <= 1500):
			ir = salario_bruto * 0.05
		elif(salario_bruto <= 2500):
			ir = salario_bruto * 0.1
		elif(salario_bruto > 2500):
			ir = salario_bruto * 0.2
	inss = salario_bruto*0.1
	total_descontos = ir+sindic+inss
	print('\nSalario bruto: R$ %.2f.'%salario_bruto)
	print('\nSindicato: R$ %.2f.'%sindic)
	print('\nIR: R$ %.2f.'%ir)
	print('\nINSS: R$ %.2f.'%(inss))
	print('\nFGTS: R$ %.2f.'%(fgts))
	print('\nTotal descontos: R$ %.2f.'%(total_descontos))
	print('\nSalario liquido: R$ %.2f.'%(salario_bruto-total_descontos))

if __name__ == '__main__':
	main()