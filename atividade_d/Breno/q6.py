nome = raw_input("Insira seu nome: ")
salario = input("Insira seu salario: ")
total_vendas = input("Insira seu total de vendas: ")
aumento = (15.0 * total_vendas) / 100.0  
salario_com_aumento = salario + aumento
print "TOTAL = %.2f" % salario_com_aumento
