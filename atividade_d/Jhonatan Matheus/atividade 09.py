#questao 9
#29/06 - jhonatan matheus
def multiplos(numero_recebido, contador_recebido):
            if((contador_recebido > 0)and(contador_recebido<=10)):
            	contador_recebido = contador_recebido + 1
            	total = numero_recebido * contador_recebido
            	print(total)
            	print(multiplos(numero_recebido,contador))
            
        
if __name__ == '__main__':
   numero = int(input("Digite um numero inteiro: "))
   contador = int(input("Digite um numero para iniciar a multiplicação a partir dele: "))
   multiplos(numero)
   
