#developed by Kairo_Costa
def calculo_salario(salario,total_vendas):
	bonus=(total_vendas/100)*15
	salario+=bonus
	return salario

def main():
	vendedor=raw_input("Insira nome vendedor: ")
	salario=input("Insira salario vendendor: ")
	vendas=input("Insira o total de vendas do vendedor: ")
	print "Total = R$ %.2f" % (calculo_salario(salario,vendas))


if __name__=="__main__":
	main()
