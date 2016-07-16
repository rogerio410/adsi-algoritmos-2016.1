def main():
	valor_hora = float(input('Digite o valor da hora do trabalhador:'))
	quant_horas = float(input('Digite a quantidade de horas trabalhadas no mes:'))
	salario_bruto = valor_hora * quant_horas
	sindicato = salario_bruto * 0.03
	fgts = salario_bruto * 0.11
	inss = salario_bruto * 0.10
	if salario_bruto <= 900:
		salario_liquido = salario_bruto - sindicato  - inss
		total_desc = salario_bruto - salario_liquido
		print 'Salario Bruto (%.2f * %.2f): %.2f' %(valor_hora,quant_horas,salario_bruto)
		print '(-) IR: ISENTO'
		print '(-) INSS(  10%%): %.2f' % inss
		print'FGTS (11%%): R$ %.2f' % fgts
		print'Total de descontos: R$ %.2f ' % total_desc
		print'Salario Liquido: R$ %.2f ' % salario_liquido
	if salario_bruto > 900 and salario_bruto <= 1500:
		ir = salario_bruto * 0.05 
		salario_liquido = salario_bruto - sindicato - inss - ir
		total_desc = salario_bruto - salario_liquido
		print 'Salario Bruto (%.2f * %.2f): %.2f' %(valor_hora,quant_horas,salario_bruto)
		print '(-) IR (5%%): %.2f' % ir
		print '(-) INSS(  10%%): %.2f' % inss
		print'FGTS (11%%): R$ %.2f' % fgts
		print'Total de descontos: R$ %.2f ' % total_desc
		print'Salario Liquido: R$ %.2f ' % salario_liquido
	if salario_bruto > 1500 and salario_bruto <= 2500:
		ir = salario_bruto * 0.10
		salario_liquido = salario_bruto - sindicato - inss - ir
		total_desc = salario_bruto - salario_liquido
		print 'Salario Bruto (%.2f * %.2f): %.2f' %(valor_hora,quant_horas,salario_bruto)
		print '(-) IR (5%%): %.2f' % ir
		print '(-) INSS(  10%%): %.2f' % inss
		print'FGTS (11%%): R$ %.2f' % fgts
		print'Total de descontos: R$ %.2f ' % total_desc
		print'Salario Liquido: R$ %.2f ' % salario_liquido
	if salario_bruto > 2500:
		ir = salario_bruto * 0.20
		salario_liquido = salario_bruto - sindicato - inss - ir
		total_desc = salario_bruto - salario_liquido
		print 'Salario Bruto (%.2f * %.2f): %.2f' %(valor_hora,quant_horas,salario_bruto)
		print '(-) IR (5%%): %.2f' % ir
		print '(-) INSS(  10%%): %.2f' % inss
		print'FGTS (11%%): R$ %.2f' % fgts
		print'Total de descontos: R$ %.2f ' % total_desc
		print'Salario Liquido: R$ %.2f ' % salario_liquido



if __name__ == '__main__':
	main()