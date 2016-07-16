from math import sqrt

def main():
	x1 = input("X1: ")
	y1 = input("Y1: ")
	x2 = input("X2: ")
	y2 = input("y2: ")
	dist_pontos(x1,y1,x2,y2)


def dist_pontos(x1,y1,x2,y2):
	d = sqrt((x2-x1)**2 + (y2-y1)**2)
	print "D:%.2f"%d

if __name__ == '__main__':
	main()
