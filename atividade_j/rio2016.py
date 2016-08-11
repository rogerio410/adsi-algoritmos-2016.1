from consultas import consultas
from medalhas import *


def main():
	cabecalho = '\n   ****** SIS - RIO 2016 ***** \n\n'
	menu = ''' 1 - Nova Medalha \n 2 - Listar Todas Medalha \n 3 - Remover Medalha 
 4 - Consultas Estatisticas \n 0 - Sair \n\n opcao >>> '''

	paises = inicializar_paises()
	medalhas = inicializar_medalhas()

	while True:
		opcao = input(cabecalho + menu)

		if opcao == 0:
			finalizar(paises)
			break
		elif opcao == 1:
			nova_medalha()
		elif opcao == 2:
			lista_todas_medalhas()
		elif opcao == 3:
			remover_medalha()
		elif opcao == 4:
			consultas()
		else:
			print "Opcao invalida"


def inicializar_paises():
	arq_paises = open('paises.txt', 'r')
	dados = arq_paises.readlines()
	paises = []
	codigo = 1
	
	if (len(dados) == 0): #importar
		arq_paises_importacao = open('paises_importacao.txt', 'r')
		for linha in arq_paises_importacao:
			temp = linha.strip().split('-')
			pais = {'id': codigo,'nome': temp[0], 'continente': temp[1], 'populacao': int(temp[2]), 'atletas': int(temp[3])}
			codigo += 1
			paises.append(pais)

		return paises

	else: #carregar paises em memoria
		pass


def inicializar_medalhas():
	pass

def finalizar(paises):
	# Gravar Paises
	arq_paises = open('paises.txt', 'w')
	for pais in paises:
		arq_paises.write(str(pais) + '\n')

	arq_paises.close()


if __name__ == '__main__':
	main()