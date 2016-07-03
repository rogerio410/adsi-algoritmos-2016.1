#coding:utf-8
### atividade 04 questão 06 ###
nome = raw_input("qual o nome do funcionário? ")
salario = input("qual o seu salário em Reais? ")
vendas = input("qual o seu número de vendas mensais? ")
"""calculo da comissão do funcionário"""
comissao = vendas*0.15
novo_salario = comissao+salario
print "%s, com salário base de R$ %.2f e receberá uma comissão de R$ %.2f por suas vendas e seu salário será de %.2f" %(nome,salario,comissao,novo_salario)
