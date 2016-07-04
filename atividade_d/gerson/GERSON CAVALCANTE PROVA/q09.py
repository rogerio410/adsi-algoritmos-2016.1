def main():
    valor = input("Digite o valor que deseja multiplicar: ")
    crescente = input("Digite o valor que deseja incrementar: ")
    tabulacao(valor, crescente)
def tabulacao(valor,crescente):
    if crescente >= 11:
        print "Fim"
    else:
        produto = valor * crescente
        print '%d X %d = %d' %(valor,crescente, produto)
        tabulacao(valor, crescente + 1)
if __name__ == '__main__':
    main()