def main():
	qtd_testes = int(input())

	for i in range(qtd_testes):
		palavras = input().split(' ')

		bubble(palavras)

		for palavra in palavras:
			print(palavra, end=' ')

		print()



def bubble(conjunto):

	for i in range(len(conjunto)): 
		trocou = False
		for j in range(len(conjunto) - i - 1):
			if tamanho_palavra(conjunto[j]) < tamanho_palavra(conjunto[j + 1]):
				temp = conjunto[j + 1]
				conjunto[j + 1] = conjunto[j]
				conjunto[j] = temp
				trocou = True
		if not trocou:
			break


def tamanho_palavra(palavra):
	tamanho = 0
	for i in palavra:
		tamanho += 1

	return tamanho

if __name__ == '__main__':
	main()