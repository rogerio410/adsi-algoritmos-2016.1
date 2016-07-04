nome_vendedor = raw_input('nome do vendedor?')
salario_fixo = input('salario fixo do usuario?')
vendas_total = input('valor total de vendas?')

salario_total = (vendas_total * 15)/100
salario_tot = salario_fixo + salario_total
print salario_tot
