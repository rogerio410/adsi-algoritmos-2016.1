
# Condicinal errada.
def media_aluno(nota_um, nota_dois):

    soma = nota_um + nota_dois
    media = soma / 2

    if media >= 7:
        print("Aprovado")
    elif media < 7:
        print("Reprovado")
    elif media == 10:
        print("Aprovado com distincao")

def main():
    nota_um = float(input("nota1: "))
    nota_dois = float(input("nota2: "))

    media_aluno(nota_um,nota_dois)


if __name__ == '__main__':
    main()
