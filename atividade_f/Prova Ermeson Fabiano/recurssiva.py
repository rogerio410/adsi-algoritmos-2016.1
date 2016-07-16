def quest16(Limite, N1, N2):
    if Limite > 0: 
        print "%d" % (N2 - N1),
        quest16(Limite - 1, N2  , N2 + N1 )
    else:
        print "FIM"

def main():
	Limite = input("Numero de Termos")
	N2	= 1
	N1 = 1
	quest16(Limite, N1, N2)

if __name__ == '__main__':
	main()