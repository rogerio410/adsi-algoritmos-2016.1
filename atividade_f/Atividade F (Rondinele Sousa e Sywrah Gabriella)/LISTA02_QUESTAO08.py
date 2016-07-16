# -*- coding: utf-8 -*-
"""
8. Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do
salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do salário bruto,
mas não é descontado (é a empresa que deposita). O salário líquido corresponde ao salário bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
o Salário Bruto até R$ 900,00 (inclusive) - isento o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10% o
Salário Bruto acima de R$ 2.500,00 - desconto de 20%
"""

#Calculando IR para salario abaixo de 900
def main():
    print 'Questão 08:'
    hora = input('Digite a quantidade de horas trabalhada: ')
    valor_hora = input('Digite o valor por hora: ')
    salario = hora * valor_hora
    fgts = salario * 0.11
    sindicato = salario * 0.03
    inss = salario * 0.1
    i_renda = 0.0
    if salario > 900 and salario <= 1500:
        i_renda = salario * 0.05
    elif salario <= 2.500:
        i_renda = salario * 0.1
    else:
        i_renda = salario * 0.2

    descontos = i_renda + inss + sindicato
    salario_liquido = salario - descontos

    print 'Salário Bruto: (%d * %d)       : R$ %.2f' %(valor_hora, hora, salario)
    print '(-)Imposto de renda: R$ %.2f' % i_renda
    print '(-)INSS: R$ %.2f' % inss
    print '(-)Sindicato: R$ %.2f' % sindicato
    print 'FGTS: R$ %.2f' % fgts
    print 'Total de descontos: R$ %.2f' % descontos
    print 'Salário líquido: R$ %.2f' % salario_liquido




if __name__ == '__main__':
    main()