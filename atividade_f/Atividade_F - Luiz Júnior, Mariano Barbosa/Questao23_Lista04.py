
def Questao23_Lista04(razao, primeiro_termo, Numero_Termos):

    cont = 0
    PG = primeiro_termo
    
    while cont < Numero_Termos:

        if cont == 0:

            print "primeiro termo: %.2f" % primeiro_termo
            cont += 1
            
        PG *= razao
        print "termo seguinte: %.2f" % PG
        cont += 1


def main():

    razao = input("Digite a razao PG: ")
    primeiro_termo = input("Digite o primeiro termo: ")
    Numero_Termos = input("Digite quantos termos deseja que sejam mostrados: ")
    Questao23_Lista04(razao, primeiro_termo, Numero_Termos)


if __name__ == "__main__":

    main()
