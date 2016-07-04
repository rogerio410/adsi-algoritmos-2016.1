def calculadora(numero,multi):
	if multi>10:
		print ("FIM")
	else:
		multi= numero+1
		total= numero*multi
		print "%d X %d = %d"%(numero,multi,total)
		multi = multi +1
		calculadora(numero,multi)
def main():
	numero=(int(input("numero")))
		
if __name__=="__main__":
	main()	
  
