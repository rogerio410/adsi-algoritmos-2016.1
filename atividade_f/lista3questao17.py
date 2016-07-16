def main():
    ene = input("insira o valor de N: ")
    fracoes(ene)

def fracoes(ene):
    fracao = 0
    for i in range(1,ene+1):
        fracao += 1.0/i
    print fracao

if __name__=="__main__":
    main()
