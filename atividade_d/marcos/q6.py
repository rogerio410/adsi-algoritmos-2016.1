print '(Questao 06) SALARIO DO FUNCIONARIO'

funcionario = raw_input ('>> Digite o nome do funcionario: ')
salario = input('>> Digite o valor do Salario Fixo do funcionario:R$ ')
vendas= input ('>> Digite o valor total das vendas do mes:R$ ')

cal_comissao= vendas*0.15 

salario_fun = cal_comissao + salario 
print 'TOTAL= R$ %.2f'%(salario_fun)
print '>> Funcionario %s recebera esse mes o valor Salario/Total R$ %.2f'%(funcionario, salario_fun)