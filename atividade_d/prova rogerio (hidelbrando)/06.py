# -*- coding: utf-8 -*-

print "QUESTÃO N°06"
nome_vendedor = raw_input("Digite o nome do vendedor: ")
salario_fixo = input("Digite o salario fixo: ")
total_de_vendas = input("Digite o total de vendas em R$: ")
porcentagem = (total_de_vendas*15)/100
salario_final = porcentagem+salario_fixo
print "TOTAL = R$ %.2f\n" % salario_final