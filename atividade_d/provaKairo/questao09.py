#developed by Kairo_Costa
def multiplos(number1,number2,times=0):
	if times<10:
		if number1%number2==0:
			print "%d eh multiplo" % (number1)
			multiplos(number1+1,number2,times+1)
		else:
			multiplos(number1+1,number2,times)

def main():
	number=input("Insira o numero que voce deseja calcular: ")
	number2=number	
	multiplos(number,number2)			
	
if __name__=="__main__":
	main()	
