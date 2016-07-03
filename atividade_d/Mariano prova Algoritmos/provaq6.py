## Mariano Barbosa de Carvalho Neto
nome = raw_input("Digite o nome do vendedor: ")
salario_fixo = input("Digite o salario do vendedor: ")
total_vendas = input("Digite o total das vendas mensais em dinheiro: ")
salario_total = (total_vendas*0.15)+salario_fixo

print "o vendedor %s recebeu um salario total de $ %.2f"%(nome,salario_total)