def main():
	valor_hora = float(input("valor da hora: "))
	qtd_hora = input("quantidade da hora: ")
	descontos(valor_hora,qtd_hora)
def descontos(valor_hora,qtd_hora):
	salario_bruto = (valor_hora*qtd_hora)
	if salario_bruto > 900.00 and salario_bruto <= 1500.00:
		IR = (salario_bruto*5)/100	
	elif salario_bruto > 1500.00 and salario_bruto <= 2500.00:
		IR = (salario_bruto*10)/100
	elif salario_bruto >  2500.00:
		IR = (salario_bruto*20)/100
	else:
		print "isento do imposto de renda"

	inss = (salario_bruto*10)/100
	fgts = (salario_bruto*11)/100
	sindicato = (salario_bruto*3)/100
	total_descontos = inss+sindicato+IR
	salario_liquido = salario_bruto - total_descontos
	print "Salario Bruto = R$ %.2f"%salario_bruto
	print "IR = R$ %.2f"%IR
	print "INSS = R$%.2f"%inss
	print "Sindicato = R$%.2f"%sindicato
	print "FGTS = R$%.2f"%fgts
	print "Total Descontos = R$%.2f"%total_descontos
	print "Salario Liquido = R$%.2f"%salario_liquido

if __name__ == '__main__':
	main()