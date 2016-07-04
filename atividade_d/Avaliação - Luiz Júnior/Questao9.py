
#Questao 9

numero = int(input())
contador = 0
for i in range(numero, numero*10+1):
    
    if i%numero==0:
        print i
        contador += 1    
        if contador == 10:
            print "Fim da conta!"
            break
        
