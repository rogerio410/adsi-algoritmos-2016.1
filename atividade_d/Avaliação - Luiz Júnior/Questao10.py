
#Questao 10

def tabuada_multiplicacao(Valor_a_ser_multiplicado, Ponto_de_Partida):

    for i in range(Ponto_de_Partida, 11):
        print "%d x %d = %d" % (Valor_a_ser_multiplicado, i, Valor_a_ser_multiplicado * i)
        if i == 10:
            print "Fim."

print tabuada_multiplicacao(6,3)
