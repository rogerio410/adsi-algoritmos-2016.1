def main():
	qtd_cartas = int(input())
	#Números cartas
	cartas = [int(i) for i in input().split(' ')]

	#arestas
	arestas = [[] for i in range(qtd_cartas)]

	for i in range(qtd_cartas - 1):
		origem, destino = [int(i) for i in input().split(' ')]
		arestas[origem - 1].append(destino - 1)
		arestas[destino - 1].append(origem - 1)

	#Percorrer o rota
	pontos = 0
	labels_verificadas = []
	for i in range(len(arestas)):
		label = cartas[i]
		if label not in labels_verificadas:
			labels_verificadas.append(label)
		else:
			continue

		visitados = []
		vizinhos = arestas[i]
		visitados.append(i)
		pts_vizinho = 0
		for vizinho in vizinhos:
			if vizinho not in visitados:
				pts_vizinho = contar(1, vizinho, visitados, arestas, label, cartas)
				if pts_vizinho > 0:
					pontos += pts_vizinho
					break

	print(pontos)


def contar(cont_atual, no, visitados, arestas, label, cartas):
	
	if label == cartas[no]:
		return cont_atual

	vizinhos = arestas[no]
	visitados.append(no)
	pontos = 0

	pts_vizinho = 0
	for vizinho in vizinhos:
		if vizinho not in visitados:
			pts_vizinho = contar(cont_atual + 1, vizinho, visitados, arestas, label, cartas)
			if pts_vizinho > 0:
				pontos += pts_vizinho
				break

	return pontos
			

if __name__ == '__main__':
	import time
	inicio = time.time()
	main()
	fim = time.time()
	print('time: %f' % (fim - inicio))

