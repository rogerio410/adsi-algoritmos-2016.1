# -*- coding:utf-8 -*-
'''A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.'''

def main():
	numero = int(input("Quantos habitantes moram aqui?: "))
	lista = range(numero)
	med_salarito = 0
	num_filhos = 0
	sal1000 = 0
	for i in lista:
		salario = float(input("Qual é o salario dele? ")) 
		filhos = int(input("Quantos filhos ele tem? "))
		med_salarito+= salario
		num_filhos+= filhos
		if salario > 1000:
			sal1000+= 1
	print ("Media do salario dele(s) é de %.1f." %(med_salarito / float(numero)))
	print ("Media de numero(s) de filho(s) é de %.1f" %(num_filhos / float(numero)))
	print ("Percentual de pessoas ganhando mais de 1000 reais é de %.1f" %((sal1000 / float(numero) * 100)))

if __name__ == '__main__':
	main()