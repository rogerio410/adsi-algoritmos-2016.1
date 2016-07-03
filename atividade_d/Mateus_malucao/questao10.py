#coding: utf-8
### atividade 04 questão 10

def tabulada_multiplicacao(x,y):
    if y <= 10:
        print "%i x %i = %i" % (x,y,(x*y))
        y = y+1
        tabulada_multiplicacao(x,y)
    else: 
        print "Fim"
valor1,valor2 = input("valores(separados por vírgula): ")
tabulada_multiplicacao(valor1,valor2) 
