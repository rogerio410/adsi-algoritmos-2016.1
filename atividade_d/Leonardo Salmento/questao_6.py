"""questao_6"""
nome = raw_input("digite o nome do vendedor: ")
salario = float(input("digite o valor do salario fixo em R$: "))
vendas = float(input("digite o total de vendas no mes: "))
salario_final = vendas * 0.15 + salario
print "salario final do vendedor sera R$ %.2f"%(salario_final)