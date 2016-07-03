#coding:utf-8
### atividade 04 questão 08 ###
print "verificar se é um triângulo"
a = input("digite  o valor do primeiro lado: ")
b = input("digite o valor do segundo lado: ")
c = input("digite o valor do terceiro lado: ")
perimetro = a+b+c
area = ((a+b)/2)*c
if (b-c) < a < b+c and (a-c) < b < a+c and (a-b) < c < a+b :
    print "é um triângulo. Perímetro = %.1f" %(perimetro)
else:	
    print "não é um triangulo e forma um trapézio de Area = %.1f " %(area)
