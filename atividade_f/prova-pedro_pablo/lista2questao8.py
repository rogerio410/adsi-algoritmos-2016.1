#__*__  encoding:utf8 __*__
"""Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
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
a quantidade de hora é 220."""


def salario_liquido(horas_trabalhadas,valor_hora):

	salario_bruto = horas_trabalhadas * valor_hora
	if salario_bruto <= 900:
		imposto_renda_valor = 0
		imposta_renda_porcentagem = "Isento"
	elif salario_bruto > 900 and salario_bruto <= 1500:
		imposto_renda_valor = salario_bruto * 0.05
		imposta_renda_porcentagem = "5%"
	elif salario_bruto > 1500 and salario_bruto <= 2500:
		imposto_renda_valor = salario_bruto * 0.10
		imposta_renda_porcentagem = "10%"
	elif salario_bruto > 2500:
		imposto_renda_valor = salario_bruto * 0.20
		imposta_renda_porcentagem = "20%"

	sindicato = salario_bruto * 0.03
	fgts = salario_bruto * 0.11
	inss = salario_bruto * 0.10
	descontos = imposto_renda_valor + sindicato + inss
	salario_liquido = salario_bruto - descontos

	print "Salario Bruto: ({} * {}): R$ {}".format(horas_trabalhadas, valor_hora, salario_bruto)	
	print "(-) IR ({}) : R$ {}".format(imposta_renda_porcentagem,imposto_renda_valor)
	print "(-) INSS ({}) : R$ {}".format("10%",inss)
	print "(-) SINDICATO ({}): R$ {}".format("3%",sindicato)
	print "FGTS ({}): R$ {}".format("11%",fgts)
	print "Total de Descontos: {}".format(descontos)
	print "Salario Liquido: R$ {}".format(salario_liquido)




def main():
	horas_trabalhadas = input("Digite as horas trabalhadas: ")
	valor_hora = input("Digite o valor da hora trabalhada: ")
	salario_liquido(horas_trabalhadas,valor_hora)

if __name__ == '__main__':
	main()