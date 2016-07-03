numero_inteiro = input("Digite um numero inteiro: ")

def funcao_recursiva(numero_inteiro, contador = 1):
	
	if contador < 11:
		print numero_inteiro*contador
		contador = contador + 1
		funcao_recursiva(numero_inteiro, contador)
	    
funcao_recursiva(numero_inteiro)