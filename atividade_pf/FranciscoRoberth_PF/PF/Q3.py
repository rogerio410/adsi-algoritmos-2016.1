def main():
	horas = ''
	minutos = ''
	segundos = ''
	hora = raw_input('Digite o horario no formato hh:mm:ss ')
	horas += hora[0]+hora[1]
	minutos += hora[3]+hora[4]
	segundos += hora[6] + hora[7]

	print '%s hora(s), %s minuto(s), %s segundo(s)'%(horas,minutos,segundos)

if __name__ == '__main__':
	main()