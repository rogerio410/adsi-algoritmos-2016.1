#coding:utf-8
### atividade 04 questão 07
valora = input("qual o valor a? ")
valorb = input("qual o valor b? ")
valorc = input("qual o valor c? ")
valord = input("qual o valor d? ")
if valorb > valorc and valord > valora and valorc+valord > valora+valorb and valorc > 0 and valord > 0 and valora%2 == 0:
    print "Valores aceitos"
else:
    print "Valores nao aceitos"
