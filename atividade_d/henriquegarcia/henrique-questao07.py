# _*_coding:utf-8_*_
#Questão 07

def valorAceito_e_naoAceito(a, b, c, d):
    if b > c:
        if d > a:
            if c + d > a + b:
                if c > 0 and d > 0:
                    if a % 2 == 0:
                        return("Valor aceito")
                    else:
                        return("Valor não aceito")


def main():
    a = int(input("Digite primeiro número: "))
    b = int(input("Digite segundo número: "))
    c = int(input("Digite terceiro número: "))
    d = int(input("Digite quarto número: "))
    valorAceito_e_naoAceito(a, b, c, d)
    print(valorAceito_e_naoAceito(a, b, c, d))


if __name__ == '__main__':
    main()
