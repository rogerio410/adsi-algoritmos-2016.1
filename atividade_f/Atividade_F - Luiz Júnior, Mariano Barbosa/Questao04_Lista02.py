
def Questao04_Lista2(Nota1, Nota2):

    media = (Nota1 + Nota2)/2.0

    if media == 10.0:

        print "Aprovado com Distincao!"
        
    elif media >= 7.0:

        print "Aprovado!"

    elif media < 7.0:

        print "Reprovado!"



def main():

    Nota1 = input("Digite a primeira nota: ")
    Nota2 = input("Digite a segunda nota: ")
    Questao04_Lista2(Nota1, Nota2)

if __name__ == "__main__":

    main()
