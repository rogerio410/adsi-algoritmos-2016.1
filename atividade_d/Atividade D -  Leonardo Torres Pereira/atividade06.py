# -*- coding: utf -8 -*-

vendedor = raw_input("Digite o nome do vendedor: ")
salario_inicial = float(input("Digite o salario inicial do vendedor em reais: "))
vendas = float(input("Digite o total de vendas em reais: "))

salario_total = salario_inicial + (vendas * 15/100)

print "O vendedor recebe no final do mes R$ %.2f " % salario_total