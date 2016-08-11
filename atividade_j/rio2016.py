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
			finalizar()
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
	pass

def inicializar_medalhas():
	pass

def finalizar():
	pass

if __name__ == '__main__':
	main()