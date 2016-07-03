#coding: utf-8

def calcula_salario(salario_fixo, vendas_efetuadas):
	salario = salario_fixo + (vendas_efetuadas*0.15)
	return salario

def main():
	salario_mensal = float(input("Digite o Valor de Salário: "))
	total_vendas = float(input("Digite o Valor do Total de Vendas: "))
	salario_liquido = calcula_salario(salario_mensal, total_vendas)
	print("A Salário Líquido é de R$ %.2f"%salario_liquido," reais.")

if __name__ == "__main__":
	main()
