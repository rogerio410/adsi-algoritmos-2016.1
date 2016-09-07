def main():

	while True:
		qtd = int(input())

		if qtd == 0: 
			break

		palavras = [] #[''] * qtd
		for i in range(qtd):
			#palavras[i] = input()
			palavras.append(input())

		palavras.sort(key=len)
		#bubble(palavras)

		#contar maior sequencia de familias de Strings
		
		maior_resultado = 0
		
		for i in range(len(palavras)):
			raiz = palavras[i]
			contador = 1
			if len(palavras) - (i + 1) < maior_resultado:
				break

			for j in range(i+1, len(palavras)):
				if raiz in palavras[j]:
					contador += 1
					raiz = palavras[j]
			
			if contador > maior_resultado:
				maior_resultado = contador

		print(maior_resultado)


def bubble(conjunto):

	for i in range(tamanho_conjunto(conjunto)): # qtd max de Execucoes é a qtd de elementos
		trocou = False
		for j in range(tamanho_conjunto(conjunto) - i - 1): # de Zero ate a Posicao nao ordenada
			if tamanho_conjunto(conjunto[j]) > tamanho_conjunto(conjunto[j + 1]):
				conjunto[j + 1], conjunto[j] = conjunto[j], conjunto[j+1]
				trocou = True
		if not trocou:
			break

def tamanho_conjunto(conjunto):
	tam = 0
	for i in conjunto:
		tam += 1

	return tam

if __name__ == '__main__':
	main()