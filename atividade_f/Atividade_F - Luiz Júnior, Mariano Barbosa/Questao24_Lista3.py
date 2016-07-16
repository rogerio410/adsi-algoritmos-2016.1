

def Questao24_Lista3(N_habitantes):

    mediaSalario = 0
    MediaFilhos = 0
    cont_Salario_Baixo = 0
    Cont_Total = 0
    
    while N_habitantes > 0:

            Salario = input("Digite o salario do trabalhador:\n ")
            N_filhos = input("Digite o numero de filhos dele:\n ")
                  
            mediaSalario += Salario
            MediaFilhos += N_filhos

            if Salario <= 1000:

                cont_Salario_Baixo += 1
                
            N_habitantes -= 1
            Cont_Total += 1

    print "A media salarial foi igual a %.2f." % (mediaSalario/float(Cont_Total))
    print "A media de filhos foi igual a %.2f." % (MediaFilhos/float(Cont_Total))
    print "O percentual de pessoas com salario menor ou igual a 1000 foi igual a %.2f. %%" % ((float(cont_Salario_Baixo)/Cont_Total)*100)




def main():

    N_habitantes = input("Digite a quantidade de habitantes: ")
   
    Questao24_Lista3(N_habitantes)


if __name__ == "__main__":

    main()
