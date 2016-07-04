#Questao 6 -



def Analista_de_Vendas(nome, salario, total_de_vendas):

    Salario_Total = salario + (total_de_vendas * 0.15)
    
    return "\nO salario a ser recebido por %s e igual a %.2f.\n" % (nome, Salario_Total)



print Analista_de_Vendas("Pedro", 600, 6000)

