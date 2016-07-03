def quest9(numero,multiplo):

  if multiplo % numero == 0:
    
    print "Multiplo %d" % multiplo
    if multiplo < numero*10:
      quest9(numero,multiplo + numero)

  else:
    print 'FIM'

if __name__ == '__main__':
  numero = input("Digite um numero")
  multiplo = numero
  quest9(numero,multiplo)
