#questao 7

numeroa = input ('coloque um numero ')
numerob = input ('coloque um numero ')
numeroc = input ('coloque um numero ')
numerod = input ('coloque um numero ')
somacd = numeroc + numerod
somaab = numeroa + numerob
if numeroc <= 0:
    print 'valores nao aceitos'
elif numerod <= 0: 
    print 'valores nao aceitos'
elif numeroa % 2 != 0:
    print 'valores nao aceitos'
elif numeroc > numerob and numerod > numeroa and somacd > somaab: 
    print 'valores aceitos'
else:
    print 'valores nao aceitos'    
