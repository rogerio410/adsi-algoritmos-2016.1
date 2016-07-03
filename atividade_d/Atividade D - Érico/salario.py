nome = raw_input("Insira seu nome: ")
salario_fixo = float(input("Insira o valor do seu salario: "))
vendas = float(input("Insira o valor das vendas do mes: "))
total = salario_fixo + vendas*0.15
print ("Total = R$ %.2f" %total)
