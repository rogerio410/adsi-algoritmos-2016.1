print "Programa para calcular salarios"
nome = raw_input("Diga o nome do funcionario:")
salariofixo = input("Diga o salario fixo desse funcionario:")
vendas = input("Quanto ele vendeu no mes?")
salariototal = salariofixo + vendas * 0.15
print "O funcionario de nome", nome, ", com um salario fixo de", salariofixo, "reais, ganhou nesse mes a quantia de", salariototal, "reais."