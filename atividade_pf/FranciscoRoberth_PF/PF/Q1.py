def main():
	fichas = []
	N = input('Quantidade fichas a serem lidas: ')

	for i in range(N):
		tamanho_lista = fichas
		fichas[tamanho(tamanho_lista):] = [cadastrar()]

	bubble_sort(fichas)

	print 'Boi mais magro:\nNro de identificacao: %d | Peso: %d |\n\nBoi mais gordo:\nNro de identificacao: %d | Peso: %d |' %(fichas[0]['Numero'],fichas[0]['Peso'],fichas[-1]['Numero'],fichas[-1]['Peso'])
def cadastrar():
	numero = input('Numero de identificacao: ')
	nome = raw_input('Nome: ')
	peso = input('Peso: ')
	cadastro = {'Numero' : numero,'Nome' : nome, 'Peso' : peso}
	return cadastro
    

def bubble_sort(lista):
    tamanho_lista = lista

    for i in range(0, tamanho(tamanho_lista)-1):
        for j in range(0, tamanho(tamanho_lista)-1-i):
            if lista[j]['Peso'] > lista[j+1]['Peso']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def tamanho(valor):
    contador = 0
    for i in valor:
        contador += 1
    return contador

if __name__ == '__main__':
	main()