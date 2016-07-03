#developed by Kairo_Costa
def mult(number1,number2):
	if number2<=10:
		multiplicacao=number1*number2
		print "%d x %d = %d" % (number1,number2,multiplicacao)
		mult(number1,number2+1)
	else:
		print "Fim."

def main():
	number1=input("Insira primeiro numero: ")
	number2=input("Insira segundo numero: ")
	mult(number1,number2)

if __name__=="__main__":
	main()	

