nome_funcionario = input('Digite o nome do funcionario:')
salario_fixo = input('Digite o salario fixo do funcionario:')
total_vendas_dinheiro = input('Digite o total de vendas efetuadas no mes:')

comissao = total_vendas_dinheiro * 0.15
total_receber_final_mes = salario_fixo + comissao


print('O total que %s deve receber no final do mes eh %.2f ') % (nome_funcionario,total_receber_final_mes) 



