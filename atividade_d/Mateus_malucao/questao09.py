#coding:utf-8
def multiplos(num,counter=1):
    if counter <= 10:
        print num*counter
        counter = counter+1
        multiplos(num,counter)
    else:
        print "acima estão os 10 múltiplos do valor" 

valor = input("qual o valor que você deseja os múltiplos? ")

multiplos(valor,counter=1)
