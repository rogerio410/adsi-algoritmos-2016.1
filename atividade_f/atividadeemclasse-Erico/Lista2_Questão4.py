def boletim(nota1, nota2):
    media = (nota1 + nota2)/2
    if media < 7:
        print ("Reprovado")
    elif media >= 7 and media < 10:
        print("Aprovado")
    else:
        print("Aprovado com Distinção")

def main():
    nota1 = float(input("Insira a primeira nota parcial: "))
    nota2 = float(input("Insira a segunda nota parcial: "))
    boletim(nota1, nota2)

if __name__ == '__main__':
    main()