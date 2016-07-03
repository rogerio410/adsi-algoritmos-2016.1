nome = raw_input('digite o nome do vendedor: ')
salario = int(input('digite o salario do vendedor: '))
vendas = int(input('digite a quantidade vendida por ele no mes: '))
comissao = vendas * 0.15
total = salario + comissao
print 'O total a ser recebio por mes eh %.2f' %(total)