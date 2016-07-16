#incompleta
def Questao17_Lista3(N):

    S = 0
    lista = []
    for i in range(1, N+1):

        if i==(N):
            
            print "1/%d = %.2f" % (i, S)
        else:
            
            print "1/%d + " % i,
            lista.append(i)
            
        S += 1.0 / i

Questao17_Lista3(5)
