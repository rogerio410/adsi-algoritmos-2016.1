def main():
    nome = raw_input('Informe o nome do vendedor: ')
    salario = float(input('Informe o salario (em R$): '))
    total_vendas = float(input('Informe o total de vendas (em R$): '))
    percentual_comissao = 0.15
    comissao_vendedor = total_vendas * percentual_comissao
    salario_total = salario + comissao_vendedor
    print 'TOTAL = R$ %.2f' %(salario_total)

if __name__ == '__main__':
	main()