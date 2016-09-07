def main():
	horas = raw_input('Digite as horas no formato hh:mm:ss : ').split(':')
	print '%s hora(s), %s minuto(s), %s segundo(s)'%(horas[0],horas[1],horas[2])

if __name__ == '__main__':
	main()