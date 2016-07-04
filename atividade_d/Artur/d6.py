print 'Programa questao 7'
nome = raw_input('Insira o nome do vendedor:\n')
sal_fixo = input('Insira o salario do vendedor:\n')
total_de_vendas = input('Insira a quantia correspondente ao total de vendas:\n')
comissao = (total_de_vendas*0.15)
sal_total = (sal_fixo+comissao)
print ('%s ira receber %.2f reais') %(nome, sal_total)