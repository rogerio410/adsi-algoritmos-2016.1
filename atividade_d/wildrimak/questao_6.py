nome_vendedor = raw_input("Infome seu nome: ")
salario_fixo = input("Informe seu salario: ")
vendas = input("Diga o total de vendas em dinheiro neste mes: ")
comissao = 0.15 * vendas
total = salario_fixo + comissao
print "Total = R$ %.2f" %(total)