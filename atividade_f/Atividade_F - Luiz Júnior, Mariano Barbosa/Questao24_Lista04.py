

def Questao24_Lista04(razao, primeiro_termo, Numero_Termos):

    cont = 0
    PA = primeiro_termo
    
    while cont < Numero_Termos:

        if cont == 0:

            print "primeiro termo: %.2f" % primeiro_termo
            cont += 1
            
        PA += razao
        print "termo seguinte: %.2f" % PA
        cont += 1


def main():

    razao = input("Digite a razao PA: ")
    primeiro_termo = input("Digite o primeiro termo: ")
    Numero_Termos = input("Digite quantos termos deseja que sejam mostrados: ")
    Questao24_Lista04(razao, primeiro_termo, Numero_Termos)


if __name__ == "__main__":

    main()
