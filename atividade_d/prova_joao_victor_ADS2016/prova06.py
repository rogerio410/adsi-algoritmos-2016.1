vendedor = raw_input('insira nome do vendedor ')
#erro desaparece quando se tira a primeira linha de codigo
valorfixo = input ('insira o salario fixo do vendedor ')
valordasvendas = input ('quanto em reais o vendedor apurou para a loja ')
comissao = valordasvendas * 15 / 100.0
salario = valorfixo + comissao
print 'total = %.d' %(salario)

