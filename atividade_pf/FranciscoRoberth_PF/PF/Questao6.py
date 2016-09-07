def main():
    alunos = []
    tabela = []
    arquivo_alunos = open('alunos.txt','r')
    linhas = arquivo_alunos.readlines()
    for linha in linhas:
        alunos.append(linha.split(';'))
    for i in alunos:
        i[3] = i[3].replace('\n', '')
        i[2] = eval(i[2])
        i[3] = eval(i[3])
    #print alunos
    for cadastro in alunos:
    	if cadastro[1] != 'E':
    		novo_cadastro = {'Nome': cadastro[0], 'Presenca' : cadastro[1], 'Nota1' : cadastro[2],'Nota2' : cadastro[3], 'Media' : ((cadastro[2] + cadastro[3])/2) +0.5}
    	else:
    		novo_cadastro = {'Nome': cadastro[0], 'Presenca' : cadastro[1], 'Nota1' : cadastro[2],'Nota2' : cadastro[3], 'Media' : ((cadastro[2] + cadastro[3])/2)}
    	tabela.append(novo_cadastro)
    menu(tabela)
def menu(alunos):
	print '|------MENU------|\n1 checar situacao alunos.\n2 Buscar por nome.\n3 Buscar por faixa de nota.\n4 Media da turma.\n0 Sair. '
	opcao = input('Digite uma opcao: ')
	if opcao == 1:
		situacao(alunos)
		menu(alunos)
	elif opcao == 2:
		listar_nome(alunos)
		menu(alunos)
	elif opcao == 3:
		listar_nota(alunos)
		menu(alunos)
	elif opcao == 4:
		media_turma(alunos)
		menu(alunos)
	elif opcao == 0:
		quit()



def situacao(alunos):
	opcao = input('Deseja limitar o numero da listagem? (1-sim 2-nao) ')
	if opcao == 1:
		quantidade = input('Digite o numero de alunos a serem exibidos: ')
	elif opcao == 2:
		quantidade = len(alunos)
	bubble_sort(alunos)
	for cadastro in range(quantidade):
		NOME = []
		NOME.append(alunos[cadastro]['Nome'].split(' '))
		if alunos[cadastro]['Presenca'] == 'E':
			print '| %s %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | EVADIDO |' %(NOME[0][0],NOME[0][-1],alunos[cadastro]['Nota1'],alunos[cadastro]['Nota2'],alunos[cadastro]['Media'])
		else:
			
			if alunos[cadastro]['Media'] >= 7:
				print '| %s %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | APROVADO |' %(NOME[0][0],NOME[0][-1],alunos[cadastro]['Nota1'],alunos[cadastro]['Nota2'],alunos[cadastro]['Media'])
			elif alunos[cadastro]['Media'] < 7 and alunos[cadastro]['Media'] >= 4:
				print '| %s %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | PROVA FINAL |' %(NOME[0][0],NOME[0][-1],alunos[cadastro]['Nota1'],alunos[cadastro]['Nota2'],alunos[cadastro]['Media'])
			else:
				print '| %s %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | REPROVADO |' %(NOME[0][0],NOME[0][-1],alunos[cadastro]['Nota1'],alunos[cadastro]['Nota2'],alunos[cadastro]['Media'])

def listar_nome(alunos):
	nome = raw_input('Digite o nome ou parte dele para efetuar a busca: ')
	for cadastro in alunos:
		if nome in cadastro['Nome'].lower():
			if cadastro['Presenca'] == 'E':
				print '| %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | EVADIDO |' %(cadastro['Nome'],cadastro['Nota1'],cadastro['Nota2'],cadastro['Media'])
			else:
				if cadastro['Media'] >= 7:
					print '| %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | APROVADO |' %(cadastro['Nome'],cadastro['Nota1'],cadastro['Nota2'],cadastro['Media'])
				elif cadastro['Media'] >= 4 and cadastro['Media'] < 7:
					print '| %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | PROVA FINAL |' %(cadastro['Nome'],cadastro['Nota1'],cadastro['Nota2'],cadastro['Media'])			
				else:
					print '| %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | REPROVADO |' %(cadastro['Nome'],cadastro['Nota1'],cadastro['Nota2'],cadastro['Media'])

def listar_nota(alunos):
	menor = input('Digite um valor minimo: ')
	maior = input('Agora digite um valor maximo: ')
	for cadastro in alunos:
		if cadastro['Media'] >= menor and cadastro['Media'] <= maior:
			if cadastro['Presenca'] == 'E':
				print '| %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | EVADIDO |' %(cadastro['Nome'],cadastro['Nota1'],cadastro['Nota2'],cadastro['Media'])
			else:
				if cadastro['Media'] >= 7:
					print '| %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | APROVADO |' %(cadastro['Nome'],cadastro['Nota1'],cadastro['Nota2'],cadastro['Media'])
				elif cadastro['Media'] >= 4 and cadastro['Media'] < 7:
					print '| %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | PROVA FINAL |' %(cadastro['Nome'],cadastro['Nota1'],cadastro['Nota2'],cadastro['Media'])			
				else:
					print '| %s | Nota 1: %.2f | Nota 2: %.2f | Media: %.2f | REPROVADO |' %(cadastro['Nome'],cadastro['Nota1'],cadastro['Nota2'],cadastro['Media'])

def media_turma(alunos):
	soma_notas = 0
	contador = 0
	for cadastro in alunos:
		if cadastro['Presenca'] != 'E':
			soma_notas += cadastro['Media']
			contador += 1
	print 'A media da turma eh: %.2f' %(soma_notas/contador)
def bubble_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1-i):
                if lista[ j ]['Media'] < lista[j + 1]['Media']:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
if __name__ == '__main__':
    main()