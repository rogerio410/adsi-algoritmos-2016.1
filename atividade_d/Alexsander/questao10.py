def tabuada(num1,num2):
	if num2 < 11:
		print'%d x %d = %d' %(num1,num2,num1*num2)
		num2 = num2+1
		tabuada(num1,num2)


def main():
	num1 = int(input('Digite a tabuada que deseja:'))
	num2 = int(input('Digite a partir de qual numero deseja:'))
	tabuada(num1,num2)


if __name__ == '__main__':
	main()
