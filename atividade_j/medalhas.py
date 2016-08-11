def nova_medalha(paises):

	tipos_medalhas = ['Ouro', 'Prata', 'Bronze'] 

	atleta = raw_input('Atleta: ')
	esporte = raw_input('Esporte: ')
	modalidade = raw_input('Masculino - Feminino - Misto: ')

	medalha = raw_input('Ouro - Prata - Bronze: ')
	while  medalha not in tipos_medalhas:
		medalha = raw_input('Ouro - Prata - Bronze: ')
	
	listar_paises(paises)
	pais_id = input('ID do Pais: ')
	while not pais_id_valido(pais_id, paises):
		pais_id = input('ID do Pais: ')

	medalha = {'atleta': atleta, 'esporte': esporte, 'modalidade': modalidade, 'medalha': medalha, 'pais_id': pais_id}

	return medalha

def pais_id_valido(pais_id, paises):
	for pais in paises:
		if pais['id'] == pais_id:
			return True

	return False

def listar_paises(paises):
	for pais in paises:
		print "%d - %s" % (pais['id'], pais['nome'])

def remover_medalha():
	pass

def lista_todas_medalhas(medalhas, paises):
	
	for medalha in medalhas:
		pais = obter_pais_por_id(medalha['pais_id'], paises)
		print "%s - %s - %s - %s" % (medalha['atleta'], medalha['esporte'], medalha['medalha'], pais['nome'])

def obter_pais_por_id(pais_id, paises):
	for pais in paises:
		if pais['id'] == pais_id:
			return pais



