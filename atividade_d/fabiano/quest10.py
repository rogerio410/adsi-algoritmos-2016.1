def tabulada_multiplicacao(numero1,numero2):
  if numero2 <= 10:
    print numero1*numero2
    tabulada_multiplicacao(numero1,numero2 + 1)
  else:
    print "Fim do programa"

if __name__ == '__main__':
  tabulada_multiplicacao(6,3)
