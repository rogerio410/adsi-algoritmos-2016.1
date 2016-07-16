def main():
	print 'Pesquisa:'
	habitantes = input('Insira a quantidade de Familias:\n')
	pesquisa_do_prefeito(habitantes)

def pesquisa_do_prefeito(habitantes):

	salario_total = 0.0
	filhos_total = 0.0
	cont_familia = 0.0
	cont_salario = 0.0
	cont_filhos = 0.0
	for x in range(habitantes):
		salario = input('Insira o salario da familia:\n')
		numero_de_filhos = input('Digite a quantidade de filhos da familia:\n')
		salario_total += salario
		cont_salario += 1
		cont_filhos += numero_de_filhos


		if salario < 1000:
			cont_familia +=1


	media = salario_total/habitantes
	media_filhos = cont_filhos/habitantes
	salario_menor = (cont_familia/habitantes)*100

	print 'A media dos salarios da populacao e %.2f' %(media)
	print 'A media do numeros e filhos da populacao e %.2f' %(media_filhos)
	print 'O percentual de pessoas com salario menor que 1000 e %d%' %(salario_menor)


if __name__ == '__main__':
	main()