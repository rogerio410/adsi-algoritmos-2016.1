# Nao mostrou a fracao resultante.
def main():
    ene = int(input("insira o valor de N: "))
    fracoes(ene)

def fracoes(ene):
    fracao = 0
    for i in range(1, ene+1):
        fracao += 1.0/i
    print("%.2f"%fracao)

if __name__ == "__main__":
    main()
