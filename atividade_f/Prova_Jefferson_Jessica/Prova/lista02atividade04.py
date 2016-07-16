'''Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
o "Aprovado", se a média alcançada for maior ou igual a sete;
o "Reprovado", se a média for menor do que sete;
o "Aprovado com Distinção", se a média for igual a dez.'''

print('Lista 02, Atividade 04')
def main():
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    media_aluno = float((nota1+nota2) / 2)
    if media_aluno >= 7 and media_aluno < 10:
        print('Aprovado!')
    elif media_aluno < 7:
        print('Reprovado')
    elif media_aluno == 10:
        print('Aprovado com Distinção')

if __name__ == '__main__':
    main()