# -*- coding:utf-8 -*-
'''Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
o Salário Bruto até R$ 900,00 (inclusive) - isento
o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$ 2.500,00 - desconto de 20%
Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00'''


# Erros de atribuicao usou == inves de = .. questao ficou errada.

def main():

	valor_hora = float(input('Valor da hora trabalhada: '))
	quanti_hora = float(input('Quantidade de horas trabalhadas: '))
	Salario = valor_hora * quanti_hora
	Sindicato = (3 / 100) * Salario
	IR = 0.0
	INSS = (10 / 100) * Salario
	FGTS = (11 / 100) * Salario
	if Salario <= 900:
		IR == 0
	elif Salario <=1500:
		IR == 5 / 100
	elif Salario <=2500:
		IR == 10 / 100
	elif Salario >2500:
		IR == 20 / 100
	total_descont = IR + INSS + Sindicato
	Salarioliqui = Salario - total_descont
	print ('IR = %.2f' %(IR)) 
	print ('INSS = %.2f' %(INSS))
	print ('FGTS = %.2f' %(FGTS))
	print ('Sindicato = %.2f' %(Sindicato))
	print ('Salario Bruto = %.2f' %(Salario))
	print ('Descontos = %.2f' %(total_descont))
	print ('Salario liquido = %.2f' %(Salarioliqui))

if __name__ == '__main__':
	main()