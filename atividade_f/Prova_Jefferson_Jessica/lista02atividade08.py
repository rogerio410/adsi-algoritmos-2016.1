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
Salário Bruto: (5 * 220)
: R$ 1100,00
(-) IR (5%)
: R$ 55,00
(-) INSS ( 10%)
: R$ 110,00
FGTS (11%)
: R$ 121,00
Total de descontos
: R$ 165,00
Salário Liquido
: R$ 935,00'''

# Muito codigo repetido.

print('Lista 02, Atividade 08')
def main():
    valor_hora = float(input('Informe o valor o valor da sua hora (R$): '))
    horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))
    salario_bruto = float(valor_hora*horas_trabalhadas)
    if salario_bruto <= 900.00:
        desconto_sindicato = salario_bruto * 0.03
        deposito_fgts = salario_bruto * 0.11
        desconto_inss = salario_bruto * (10 / 100)
        salario_liquido = salario_bruto - desconto_inss - desconto_sindicato
        total_descontos = desconto_inss + desconto_sindicato
        print('Salário Bruto: %.2f' % salario_bruto)
        print('Desconto do IR: Sem Descontos')
        print('Desconto do Sindicato: %.2f' % desconto_sindicato)
        print('Desconto do INSS: %.2f' % desconto_inss)
        print('Depósito do FGTS: %.2f' % deposito_fgts)
        print('Total de descontos: %.2f' % total_descontos)
        print('Salário Líquido: %.2f' % salario_liquido)
    elif salario_bruto > 900.00 and salario_bruto <= 1500.00:
        desconto_sindicato = salario_bruto * 0.03
        deposito_fgts = salario_bruto * 0.11
        desconto_ir = salario_bruto * 0.05
        desconto_inss = salario_bruto * (10/100)
        salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
        total_descontos =  desconto_inss + desconto_ir + desconto_sindicato
        print('Salário Bruto: %.2f' % salario_bruto)
        print('Desconto do IR: %.2f' % desconto_ir)
        print('Desconto do Sindicato: %.2f' % desconto_sindicato)
        print('Desconto do INSS: %.2f' % desconto_inss)
        print('Depósito do FGTS: %.2f' % deposito_fgts)
        print('Total de descontos: %.2f' % total_descontos)
        print('Salário Líquido: %.2f' % salario_liquido)
    elif salario_bruto > 1500.00 and salario_bruto <= 2500.00:
        desconto_sindicato = salario_bruto * 0.03
        deposito_fgts = salario_bruto * 0.11
        desconto_ir = salario_bruto * 0.10
        desconto_inss = salario_bruto * (10 / 100)
        salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
        total_descontos = desconto_inss + desconto_ir + desconto_sindicato
        print('Salário Bruto: %.2f' % salario_bruto)
        print('Desconto do IR: %.2f' % desconto_ir)
        print('Desconto do Sindicato: %.2f' % desconto_sindicato)
        print('Desconto do INSS: %.2f' % desconto_inss)
        print('Depósito do FGTS: %.2f' % deposito_fgts)
        print('Total de descontos: %.2f' % total_descontos)
        print('Salário Líquido: %.2f' % salario_liquido)
    else:
        desconto_sindicato = salario_bruto * 0.03
        deposito_fgts = salario_bruto * 0.11
        desconto_ir = salario_bruto * 0.20
        desconto_inss = salario_bruto * (10 / 100)
        salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
        total_descontos = desconto_inss + desconto_ir + desconto_sindicato
        print('Salário Bruto: %.2f' % salario_bruto)
        print('Desconto do IR: %.2f' % desconto_ir)
        print('Desconto do Sindicato: %.2f' % desconto_sindicato)
        print('Desconto do INSS: %.2f' % desconto_inss)
        print('Depósito do FGTS: %.2f' % deposito_fgts)
        print('Total de descontos: %.2f' % total_descontos)
        print('Salário Líquido: %.2f' % salario_liquido)



if __name__ == '__main__':
    main()