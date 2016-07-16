def main():
	numero = input("Voce quer inserir as informacoes de quantos funcionarios? ")
	lista = range(numero)
	for i in lista:
		codigo = input("Qual e o codigo do funcionario? ")
		horastrabalhadas = float(input("Quantas horas ele trabalha? "))
		dependentes = input("Quantos depedentes ele tem? ")
		salario = (horastrabalhadas * 12) + (dependentes * 40)
		inss = salario * 0.085
		ir = salario * 0.05
		salarioliquido = salario - (inss + ir)
		print "Funcionario:", codigo
		print "INSS:", inss, "reais"
		print "IR:", ir, "reais"
		print "Salario liquido:", salarioliquido, "reais"

if __name__ == '__main__':
	main()