#Incompleta
def Questao16_Lista3(Numero):

    a = 0; b = 1
    cont = 0
    
    while cont<Numero:

        print a,
        a = b
        b += a
        cont += 1

Questao16_Lista3(5)
