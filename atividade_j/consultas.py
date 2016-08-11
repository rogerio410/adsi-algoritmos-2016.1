from medalhas import obter_pais_por_id


def consultas(medalhas, paises):
	cabecalho = "\n **** Consultas e Estatisticas **** \n"
	menu_consulta = " 1 - Medalhas por Pais \n 2 - Medalhas por Continente \n 0 - Voltar \n opcao >>> "

	while True:
		opcao = input(cabecalho + menu_consulta)

		if opcao == 0:
			return
		elif opcao == 1:
			medalhas_por_pais(medalhas, paises)
		elif opcao == 2:
			medalhas_por_continente(medalhas, paises)
		else:
			print 'Opcao invalida.'


def medalhas_por_pais(medalhas, paises):

	for pais in paises:
		qtd_ouro = qtd_medalha_por_pais(medalhas, pais['id'], 'Ouro')
		qtd_prata = qtd_medalha_por_pais(medalhas, pais['id'], 'Prata')
		qtd_bronze = qtd_medalha_por_pais(medalhas, pais['id'], 'Bronze')
		print '%s -> Ouro: %d -> Prata: %d -> Bronze: %d' % (pais['nome'], qtd_ouro, qtd_prata, qtd_bronze )


def qtd_medalha_por_pais(medalhas, pais_id, tipo_medalha):
	qtd = 0
	for medalha in medalhas:
		if medalha['pais_id'] == pais_id and medalha['medalha'] == tipo_medalha:
			qtd += 1

	return qtd


def medalhas_por_continente(medalhas, paises):
	continentes = ['AMERICA', 'EUROPA', 'ASIA', 'OCEANIA', 'AFRICA']

	for continente in continentes:
		qtd_ouro = qtd_medalha_por_continente(medalhas, paises, continente, 'Ouro')
		qtd_prata = qtd_medalha_por_continente(medalhas, paises, continente, 'Prata')
		qtd_bronze = qtd_medalha_por_continente(medalhas, paises, continente, 'Bronze')
		print '%s -> Ouro: %d -> Prata: %d -> Bronze: %d' % (continente, qtd_ouro, qtd_prata, qtd_bronze )


def qtd_medalha_por_continente(medalhas, paises, continente, tipo_medalha):
	qtd = 0

	for medalha in medalhas:
		pais = obter_pais_por_id(medalha['pais_id'], paises)
		if pais['continente'] == continente and medalha['medalha'] == tipo_medalha:
			qtd += 1

	return qtd
