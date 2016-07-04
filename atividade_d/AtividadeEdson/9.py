def mult(nume):
	cont = 0
	if cont > 10:
		print("FIM")
	else:
		nume = nume +nume
		print nume
		mult(nume)+1
		cont = cont +1
def main():
	nume=(int(input("escreva um numero")))
	mult(nume)
if __name__ == '__main__':
	main()	
  
