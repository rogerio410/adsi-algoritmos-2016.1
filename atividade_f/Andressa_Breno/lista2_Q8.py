#-*- coding: utf-8 -*-

# Sindicato? <900 so isento de IR

def calculo(valor,hora,qnt):
	salario = hora * qnt
	sindicato = salario * 0.03
	ir = salario * valor 
	inss = salario * 0.1
	fgts = salario * 0.11
	desconto = (ir + inss + sindicato)
	liquido = salario - desconto
	print "Salario Bruto: (%.2f * %.2f): R$ %.2f " % (hora, qnt, salario)
	print "IR -%.1f: R$ %.2f" % (valor, ir)
	print "INSS -10 R$ %.2f" % (inss)
	print "FGTS(11): R$ %.2f" % (fgts)
	print "Total de descontos: R$ %.2f" % desconto
	print "Salário liquido: R$ %.2f" % liquido
 


def main():
	hora = input('valor da sua hora: ')
	qnt = input('quantidade de horas trabalhadas no mês: ')
	salario = hora * qnt
	if salario <= 900.00:
		print "Isento"
	elif salario <= 1500.00:
		calculo(0.05,hora,qnt)
	elif salario <= 2500.00:
		calculo(0.1,hora,qnt)
	elif salario > 2500.00:
		calculo(0.2,hora,qnt)

if __name__ == '__main__':
	main()