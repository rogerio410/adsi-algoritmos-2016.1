# -*- coding:utf-8 -*-
'''Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
o "Aprovado", se a média alcançada for maior ou igual a sete;
o "Reprovado", se a média for menor do que sete;
o "Aprovado com Distinção", se a média for igual a dez.'''
def main():

	nota1, nota2 = float(input('Ínsira a nota: ')), float(input('Ínsira a nota: '))
	
	media = (nota1 + nota2) / 2
	
	if media == 10:
		print ('Aprovado com Distinção')
	
	elif media >= 7:
		print ('Aprovado')
	
	else:
		print('Reprovado')

if __name__ == '__main__':
	main()