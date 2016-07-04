#6 question
#29/06 - jhonatan matheus
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salario fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas(em dinheiro): "))
total_receber = float(salario_fixo + (total_vendas * 0.15))
print("O vendedor "+nome_vendedor+" vai ganhar: R$ %.2f"%(round(total_receber, 2)))
