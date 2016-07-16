
def main():
	salario()
	filhos()
	percentual()



def salario():
	
	soma_habitantes = 0
	contador_habitantes = 0
	media = 0
	salario_habitante = input("Digite o salario:")
	contador_percentual = 0
	calculo_percentual = 0
	while salario_habitante != 0:
		soma_habitantes = soma_habitantes + salario_habitante
		contador_habitantes += 1
		media = soma_habitantes/contador_habitantes
		salario_habitante = input("Digite o salario:")
		if salario_habitante <= 1000:
			contador_percentual += 1
	print "A media de salarios da populacao %d" %(media)
	calculo_percentual = ((contador_percentual*10)/contador_habitantes)*10
	print  "O percentual eh igual a :%d %%" %(calculo_percentual)


def filhos():
	filhos_habitantes = input("Quantos filhos voce tem:")
	soma_filhos = 0
	contador_filhos = 0
	media_filhos = 0 
	while filhos_habitantes != 0:
		soma_filhos = soma_filhos + filhos_habitantes
		contador_filhos += 1
		media_filhos = soma_filhos/contador_filhos
		filhos_habitantes = input("Quantos filhos voce tem:")

	print"A media de filhos por familia eh %d" %(media_filhos)


if __name__ == '__main__':
	main()