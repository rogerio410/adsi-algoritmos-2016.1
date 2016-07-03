
valor1 = input()
valor2 = input()
valor3 = input()

if (valor2-valor3)<valor1<(valor2+valor3) and  (valor1-valor3)<valor2<(valor1+valor3) and (valor1-valor2)<valor3<(valor1+valor2):

    perimetro = (valor1*valor2*valor3)/2.0
    
    print "Perimetro = %.2f." % perimetro

else:

    Area = ((valor1+valor2)*valor3)/2.0
    
    print "Area = %.2f." % Area

    

    
