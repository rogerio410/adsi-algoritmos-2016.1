def main():
    menu = "1 - adicionar\n2 - listar\n3 - remover\n4 - sair\n operacao: "

    bd_olimpiadas = inicio()

    while True:
        opcao = input(menu)
        if opcao == 1:
            cadastro = adicionar_atleta()
            bd_olimpiadas.append(cadastro)
            print "Atleta ou equipe cadastrada ..."
        elif opcao == 2:
            listarCadastro(bd_olimpiadas)
        elif opcao == 3:
            RemoverRegistros(bd_olimpiadas)
        else:
            finalizar(bd_olimpiadas)
            print "FINALIZANDO CADASTRO ..."
            break


def inicio():
    arquivo_cadastro = open("cadastro.txt", "r")
    linhas_cadastro = arquivo_cadastro.readlines()
    cadastro = []
    for linha in linhas_cadastro:
        cadastro.append(eval(linha))
    arquivo_cadastro.close()
    return cadastro


def finalizar(lista):
    arquivo = open("cadastro.txt", "w")
    for atleta in lista:
        arquivo.write(str(atleta) + "\n")
    arquivo.close()


def adicionar_atleta():
    nome_atleta = raw_input("nome do atleta ou equipe: ")
    esporte = raw_input("esporte: ")
    modalidade = raw_input("modalidade(masculino,feminino,misto): ")
    medalha = raw_input("medalha: ")
    pais = raw_input("pais: ")
    atleta = {"nome_atleta": nome_atleta, "esporte": esporte, "modalidade": modalidade, "medalha": medalha,
              "pais": pais}
    return atleta


# if medalha in medalhas:
#	return atleta


#	for i in importarPaises():
#	if pais == i:
#		return atleta
#	else:
#		print " Pais do atleta nao esta nas olimpiadas"



def listarCadastro(bd_olimpiadas):
    print "##################################$#########################################"
    print "Possui %d cadastros no banco de dados " % len((bd_olimpiadas))
    for i in range(len(bd_olimpiadas)):
        # print "##################################$#########################################"
        # print"--- Atleta|esporteorte|Modalidade|Medalha|Pais ------"
        print i, bd_olimpiadas[i]['nome_atleta'], bd_olimpiadas[i]['esporte'], bd_olimpiadas[i]['modalidade'], \
        bd_olimpiadas[i]['medalha'], bd_olimpiadas[i]['pais']
    # print "\n"


def RemoverRegistros(bd_olimpiadas):
    listarCadastro(bd_olimpiadas)
    indice = input("Qual indice deseja remover?: ")
    remove = bd_olimpiadas.pop(indice)
    print  'Atleta ', remove['nome_atleta'], ' removido.'


def importarPaises():
    arquivo_paises = open("paises.txt", "r")
    linhas = arquivo_paises.readlines()
    paises = []
    for linha in linhas:
        paises.append(eval(linha))

    arquivo_paises.close()

    return paises


if __name__ == '__main__':
    main()
