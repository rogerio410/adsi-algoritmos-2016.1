#-*- coding: utf-8 -*-	
def media(nota1,nota2):
	media = (nota1+nota2) / 2
	if media >= 7:
		print 'Aprovado'
	elif media < 7:
		print 'Reprovado'
	elif media == 10:
		print 'Aprovado com Distinção' 

def main():
	nota1 = input('Insira sua primeira nota: ')
	nota2 = input('Insira sua segunda nota: ')
	media(nota1,nota2)	

if __name__ == '__main__':
	main()