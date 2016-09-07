def main():
	magro = {}
	gordo = {}
	N = input('Quantidade fichas a serem lidas: ')
	for i in range(N):
		numero = input('Numero de identificacao: ')
		nome = raw_input('Nome: ')
		peso = input('Peso: ')
		cadastro = {'Numero' : numero,'Nome' : nome, 'Peso' : peso}
		if len(magro) == 0:
			magro = cadastro
		else:
			if magro['Peso'] > cadastro['Peso']:
				magro = cadastro
		if len(gordo) == 0:
			gordo = cadastro
		else:
			if gordo['Peso'] < cadastro['Peso']:
				gordo = cadastro

	print 'Boi mais magro:\nNro de identificacao: %d | Peso: %d |\n\nBoi mais gordo:\nNro de identificacao: %d | Peso: %d |' %(magro['Numero'],magro['Peso'],gordo['Numero'],gordo['Peso'])

if __name__ == '__main__':
	main()